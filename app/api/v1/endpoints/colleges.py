from fastapi import APIRouter, HTTPException, Query, Depends, status
from typing import List, Optional
from beanie import PydanticObjectId
from app.models.college import College
from app.schemas.base import BaseResponseSchema
from app.services.college_service import CollegeService

router = APIRouter()


@router.get(
    "/",
    response_model=BaseResponseSchema,
    summary="Get list of colleges",
    description="Retrieve colleges with optional filtering, sorting, and pagination"
)
async def get_colleges(
    search: Optional[str] = Query(
        None,
        description="Search by college name (case-insensitive)",
        min_length=2,
        max_length=100
    ),
    state: Optional[str] = Query(
        None,
        description="Filter by state (e.g., Delhi, Karnataka, Maharashtra)"
    ),
    type: Optional[str] = Query(
        None,
        description="Filter by college type (Public or Private)"
    ),
    category: Optional[str] = Query(
        None,
        description="Filter by category (e.g., Engineering, Medical, Management)"
    ),
    sort_by: Optional[str] = Query(
        None,
        description="Sort by field",
        pattern="^(ranking|rating|fees|placement)$",
        alias="sortBy"
    ),
    page: int = Query(
        1,
        ge=1,
        description="Page number (starts from 1)"
    ),
    limit: int = Query(
        10,
        ge=1,
        le=100,
        description="Number of items per page (max 100)"
    ),
) -> BaseResponseSchema:
    """
    Get colleges with optional filters and pagination.
    """
    try:
        print("query params:", {
            "search": search,
            "state": state,
            "type": type,
            "category": category,
            "sort_by": sort_by,
            "page": page,
            "limit": limit
        })
        # Build query filters
        query = {}
        
        if search:
            search = search.strip()
            query["name"] = {"$regex": search, "$options": "i"}
        
        if state:
            query["state"] = state.strip()
        
        if type:
            valid_types = ["Public", "Private"]
            if type not in valid_types:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid type. Must be one of: {', '.join(valid_types)}"
                )
            query["type"] = type
        
        if category:
            query["category"] = category.strip()
        
        # Build sort criteria
        sort_criteria = None
        if sort_by:
            sort_fields = {
                "ranking": "ranking",
                "rating": "rating",
                "fees": "fees",
                "placement": "placement",
            }
            sort_field = sort_fields.get(sort_by)
            sort_order = -1  # Descending order
            sort_criteria = [(sort_field, sort_order)]
        
        # Fetch colleges from service
        colleges_data = await CollegeService.get_colleges(
            query=query,
            sort_criteria=sort_criteria,
            page=page,
            page_size=limit
        )
        
        return BaseResponseSchema(
            success=True,
            message="Colleges retrieved successfully",
            data=colleges_data.model_dump()
        )
    
    except HTTPException:
        raise
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching colleges"
        )


@router.get(
    "/{id}",
    response_model=BaseResponseSchema
)
async def get_college(id: int) -> BaseResponseSchema:
    college_data = await CollegeService.get_college_data(id)
    if not college_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="College not found"
        )
    return BaseResponseSchema(
        success=True,
        message="College retrieved successfully",
        data=college_data
    )

# ----------------------------------
# Get College Details
# ----------------------------------
@router.get("/{id}/details", response_model=BaseResponseSchema)
def get_college_details(id: int) -> BaseResponseSchema:
    college_basic_info = CollegeService.get_college_details(id)
    return BaseResponseSchema(
        success=True,
        message="College details retrieved successfully",
        data=college_basic_info
    )


# ----------------------------------
# Get College Ratings
# ----------------------------------
@router.get("/{id}/ratings", response_model=BaseResponseSchema)
def get_college_ratings(id: int) -> BaseResponseSchema:
    ratings = CollegeService.get_college_ratings(id)
    return BaseResponseSchema(
        success=True,
        message="College ratings retrieved successfully",
        data=ratings
    )


# ----------------------------------
# Get College Reviews
# ----------------------------------
@router.get("/{id}/reviews", response_model=BaseResponseSchema)
def get_college_reviews_endpoint(id: int) -> BaseResponseSchema:
    reviews = CollegeService.get_college_reviews(id)
    return BaseResponseSchema(
        success=True,
        message="College reviews retrieved successfully",
        data=reviews
    )


# ----------------------------------
# Get Fee Structure
# ----------------------------------
@router.get("/{id}/fees", response_model=BaseResponseSchema)
def get_fee_structure(id: int) -> BaseResponseSchema:
    fees = CollegeService.get_fee_structure(id)
    return BaseResponseSchema(
        success=True,
        message="College fee structure retrieved successfully",
        data=fees
    )


# ----------------------------------
# Get Placement Data
# ----------------------------------
@router.get("/{id}/placements", response_model=BaseResponseSchema)
def get_placements(id: int) -> BaseResponseSchema:
    placements = CollegeService.get_placements(id)
    return BaseResponseSchema(
        success=True,
        message="College placement data retrieved successfully",
        data=placements
    )


# ----------------------------------
# Get Branch-wise Placements
# ----------------------------------
@router.get("/{id}/placements/branches", response_model=BaseResponseSchema)
def get_branch_placements(id: int) -> BaseResponseSchema:
    placement_branches = CollegeService.get_branch_placements(id)
    return BaseResponseSchema(
        success=True,
        message="College branch-wise placement data retrieved successfully",
        data=placement_branches
    )


# ----------------------------------
# Get Admission Information
# ----------------------------------
@router.get("/{id}/admissions", response_model=BaseResponseSchema)
def get_admissions(id: int) -> BaseResponseSchema:
    admissions = CollegeService.get_admissions(id)
    return BaseResponseSchema(
        success=True,
        message="College admission information retrieved successfully",
        data=admissions
    )


# ----------------------------------
# Get Academic Information
# ----------------------------------
@router.get("/{id}/academics", response_model=BaseResponseSchema)
def get_academics(id: int) -> BaseResponseSchema:
    academics = CollegeService.get_academics(id)
    return BaseResponseSchema(
        success=True,
        message="College academic information retrieved successfully",
        data=academics
    )


# ----------------------------------
# Get Departments
# ----------------------------------
@router.get("/{id}/departments", response_model=BaseResponseSchema)
def get_departments(id: int) -> BaseResponseSchema:
    departments = CollegeService.get_departments(id)
    return BaseResponseSchema(
        success=True,
        message="College departments retrieved successfully",
        data=departments
    )


# ----------------------------------
# Get Infrastructure
# ----------------------------------
@router.get("/{id}/infrastructure", response_model=BaseResponseSchema)
def get_infrastructure(id: int) -> BaseResponseSchema:
    infrastructure = CollegeService.get_infrastructure(id)
    return BaseResponseSchema(
        success=True,
        message="College infrastructure retrieved successfully",
        data=infrastructure
    )


# ----------------------------------
# Get Campus Experience
# ----------------------------------
@router.get("/{id}/campus-experience", response_model=BaseResponseSchema)
def get_campus_experience(id: int) -> BaseResponseSchema:
    experience = CollegeService.get_campus_experience(id)
    return BaseResponseSchema(
        success=True,
        message="College campus experience retrieved successfully",
        data=experience
    )


# ----------------------------------
# Get Clubs
# ----------------------------------
@router.get("/{id}/clubs", response_model=BaseResponseSchema)
def get_clubs(id: int) -> BaseResponseSchema:
    clubs = CollegeService.get_clubs(id)
    return BaseResponseSchema(
        success=True,
        message="College clubs retrieved successfully",
        data=clubs
    )


# ----------------------------------
# Get Events
# ----------------------------------
@router.get("/{id}/events", response_model=BaseResponseSchema)
def get_events(id: int) -> BaseResponseSchema:
    events = CollegeService.get_events(id)
    return BaseResponseSchema(
        success=True,
        message="College events retrieved successfully",
        data=events
    )


# ----------------------------------
# Get Gallery Images
# ----------------------------------
@router.get("/{id}/gallery", response_model=BaseResponseSchema)
def get_gallery(id: int) -> BaseResponseSchema:
    gallery = CollegeService.get_gallery(id)
    return BaseResponseSchema(
        success=True,
        message="College gallery images retrieved successfully",
        data=gallery
    )


# ----------------------------------
# Get Alumni Network
# ----------------------------------
@router.get("/{id}/alumni", response_model=BaseResponseSchema)
def get_alumni(id: int) -> BaseResponseSchema:
    alumni = CollegeService.get_alumni(id)
    return BaseResponseSchema(
        success=True,
        message="College alumni network retrieved successfully",
        data=alumni
    )


# ----------------------------------
# Get Scholarships
# ----------------------------------
@router.get("/{id}/scholarships", response_model=BaseResponseSchema)
def get_scholarships(id: int) -> BaseResponseSchema:
    scholarships = CollegeService.get_scholarships(id)
    return BaseResponseSchema(
        success=True,
        message="College scholarships retrieved successfully",
        data=scholarships
    )


# ----------------------------------
# Get News (with filtering, sorting, and pagination)
# ----------------------------------
@router.get("/{id}/news", response_model=BaseResponseSchema)
def get_news(
    id: int,
    search: Optional[str] = Query(
        None,
        description="Search news by title or content (case-insensitive)",
        min_length=2,
        max_length=100
    ),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
):
    news = CollegeService.get_news(id, search, page, limit)
    return BaseResponseSchema(
        success=True,
        message="College news retrieved successfully",
        data=news
    )


# ----------------------------------
# Get Startups
# ----------------------------------
@router.get("/{id}/startups", response_model=BaseResponseSchema)
def get_startups(id: int) -> BaseResponseSchema:
    startups = CollegeService.get_startups(id)
    return BaseResponseSchema(
        success=True,
        message="College startups retrieved successfully",
        data=startups
    )


# ----------------------------------
# Get Social Media Links
# ----------------------------------
@router.get("/{id}/social-media", response_model=BaseResponseSchema)
def get_social_media(id: int) -> BaseResponseSchema:
    social_media = CollegeService.get_social_media(id)
    return BaseResponseSchema(
        success=True,
        message="College social media links retrieved successfully",
        data=social_media
    )


# ----------------------------------
# Get Nearby Places
# ----------------------------------
@router.get("/{id}/nearby-places", response_model=BaseResponseSchema)
def get_nearby_places(id: int) -> BaseResponseSchema:
    nearby_places = CollegeService.get_nearby_places(id)
    return BaseResponseSchema(
        success=True,
        message="College nearby places retrieved successfully",
        data=nearby_places
    )


# ----------------------------------
# Get Startups
# ----------------------------------
@router.get("/{id}/startups", response_model=BaseResponseSchema)
def get_startups(id: int) -> BaseResponseSchema:
    startups = {
            "startups": [
                {"id": "st1", "name": "Alpha Robotics", "founder": "Riya Sharma", "description": "Autonomous indoor robots for logistics.", "funding": "INR 1.8 crores Seed", "image": "https://picsum.photos/seed/startup1/800/400"},
                {"id": "st2", "name": "GreenGrid", "founder": "Arjun Patel", "description": "Solar microgrid optimization platform.", "funding": "INR 90 lakhs Angel", "image": "https://picsum.photos/seed/startup2/800/400"}
            ]
        }
    return BaseResponseSchema(
        success=True,
        message="College startups retrieved successfully",
        data=startups
    )


# ----------------------------------
# Get Social Media Links
# ----------------------------------
@router.get("/{id}/social-media", response_model=BaseResponseSchema)
def get_social_media(id: int) -> BaseResponseSchema:
    media = {
        "official": {
            "facebook": "https://facebook.com/nita.official",
            "twitter": "https://twitter.com/nita_official",
            "instagram": "https://instagram.com/nita_official",
            "youtube": "https://youtube.com/@nita_official",
            "linkedin": "https://linkedin.com/school/nita"
        }
    }
    return BaseResponseSchema(
        success=True,
        message="College social media links retrieved successfully",
        data=media
    )


# ----------------------------------
# Get Nearby Places
# ----------------------------------
@router.get("/{id}/nearby-places", response_model=BaseResponseSchema)
def get_nearby_places(id: int) -> BaseResponseSchema:
    places = {
        "places": [
            {"id": "np1", "name": "Dadri Railway Station", "distance": "4.2 km", "type": "Transport"},
            {"id": "np2", "name": "Shopping Mall Delta", "distance": "3.5 km", "type": "Shopping"},
            {"id": "np3", "name": "City Hospital Prime", "distance": "2.0 km", "type": "Healthcare"}
        ]
    }
    return BaseResponseSchema(
        success=True,
        message="College nearby places retrieved successfully",
        data=places
    )
