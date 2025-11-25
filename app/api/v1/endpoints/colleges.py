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


@router.get("/{id}", response_model=BaseResponseSchema)
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


