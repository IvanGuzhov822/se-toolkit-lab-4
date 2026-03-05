"""Unit tests for edge cases and boundary values.
"""

from app.models.interaction import InteractionLog, InteractionLogCreate
from app.models.item import ItemCreate, ItemUpdate
from app.models.learner import LearnerCreate
from app.routers.interactions import filter_by_max_item_id




def test_interaction_log_create_with_empty_kind() -> None:
    """Test creating InteractionLogCreate with empty string for kind field.
    
    Existing tests use kind="attempt" but don't test empty string validation.
    This verifies Pydantic allows empty strings (no min_length constraint).
    """
    log_create = InteractionLogCreate(learner_id=1, item_id=1, kind="")
    assert log_create.kind == ""
    assert log_create.learner_id == 1
    assert log_create.item_id == 1


def test_item_create_with_zero_parent_id() -> None:
    """Test ItemCreate with parent_id=0 (different from None).
    
    parent_id=None means no parent, but parent_id=0 could be ambiguous.
    This test verifies how the model handles zero as parent_id.
    """
    item = ItemCreate(type="task", parent_id=0, title="Test Item")
    assert item.parent_id == 0


def test_item_update_with_empty_description() -> None:
    """Test ItemUpdate accepts empty description string.
    
    Empty description is a valid boundary case different from None.
    """
    update = ItemUpdate(title="New Title", description="")
    assert update.description == ""
    assert update.title == "New Title"
