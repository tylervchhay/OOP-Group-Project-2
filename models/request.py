# models/request.py

from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any

from utils.validation import (
    validate_non_empty,
    validate_request_type,
    validate_urgency,
    validate_status,
    validate_float,
    validate_int_optional,
)


@dataclass
class Request:
    # Core fields
    request_id: str
    requester_name: str
    location: str
    request_type: str
    urgency_level: str
    estimated_cost: float
    status: str

    # Type-specific fields (optional)
    issue_type: Optional[str] = None
    days_open: Optional[int] = None

    expected_attendees: Optional[int] = None
    event_date: Optional[str] = None  # keep as string

    hazard_level: Optional[str] = None
    response_time_minutes: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict[str, str]) -> "Request":
        # Core fields with validation
        request_id = validate_non_empty(data.get("request_id", ""), "Request ID")
        requester_name = validate_non_empty(data.get("requester_name", ""), "Requester name")
        location = validate_non_empty(data.get("location", ""), "Location")
        request_type = validate_request_type(data.get("request_type", ""))
        urgency_level = validate_urgency(data.get("urgency_level", ""))
        estimated_cost = validate_float(data.get("estimated_cost", ""), "Estimated cost")
        status = validate_status(data.get("status", ""))

        # Optional / type-specific
        issue_type = (data.get("issue_type") or "").strip() or None
        days_open = validate_int_optional(data.get("days_open", ""), "Days open")

        expected_attendees = validate_int_optional(
            data.get("expected_attendees", ""), "Expected attendees"
        )
        event_date = (data.get("event_date") or "").strip() or None

        hazard_level = (data.get("hazard_level") or "").strip() or None
        response_time_minutes = validate_int_optional(
            data.get("response_time_minutes", ""), "Response time (minutes)"
        )

        return Request(
            request_id=request_id,
            requester_name=requester_name,
            location=location,
            request_type=request_type,
            urgency_level=urgency_level,
            estimated_cost=estimated_cost,
            status=status,
            issue_type=issue_type,
            days_open=days_open,
            expected_attendees=expected_attendees,
            event_date=event_date,
            hazard_level=hazard_level,
            response_time_minutes=response_time_minutes,
        )
