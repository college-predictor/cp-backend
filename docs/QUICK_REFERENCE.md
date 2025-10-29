# College API - Quick Reference Guide

## Base URL
```
http://localhost:8000/api/v1/colleges
```

## All Endpoints

| # | Endpoint | Method | Description |
|---|----------|--------|-------------|
| 1 | `/` | GET | List all colleges with filters |
| 2 | `/{id}` | GET | Get complete college data |
| 3 | `/{id}/details` | GET | Get college details |
| 4 | `/{id}/ratings` | GET | Get college ratings |
| 5 | `/{id}/reviews` | GET | Get college reviews |
| 6 | `/{id}/fees` | GET | Get fee structure |
| 7 | `/{id}/placements` | GET | Get placement statistics |
| 8 | `/{id}/placements/branches` | GET | Get branch-wise placements |
| 9 | `/{id}/admissions` | GET | Get admission information |
| 10 | `/{id}/academics` | GET | Get academic information |
| 11 | `/{id}/departments` | GET | Get departments |
| 12 | `/{id}/infrastructure` | GET | Get infrastructure details |
| 13 | `/{id}/campus-experience` | GET | Get campus life info |
| 14 | `/{id}/clubs` | GET | Get student clubs |
| 15 | `/{id}/events` | GET | Get college events |
| 16 | `/{id}/gallery` | GET | Get photo gallery |
| 17 | `/{id}/alumni` | GET | Get alumni network |
| 18 | `/{id}/scholarships` | GET | Get scholarships |
| 19 | `/{id}/news` | GET | Get college news |
| 20 | `/{id}/startups` | GET | Get student startups |
| 21 | `/{id}/social-media` | GET | Get social media links |
| 22 | `/{id}/nearby-places` | GET | Get nearby places |

## Quick Examples

### 1. Get all colleges
```bash
curl http://localhost:8000/api/v1/colleges
```

### 2. Search colleges by name
```bash
curl "http://localhost:8000/api/v1/colleges?search=IIT"
```

### 3. Filter by state and type
```bash
curl "http://localhost:8000/api/v1/colleges?state=Delhi&type=Public"
```

### 4. Get college details
```bash
curl http://localhost:8000/api/v1/colleges/1/details
```

### 5. Get placements
```bash
curl http://localhost:8000/api/v1/colleges/1/placements
```

### 6. Get news with search
```bash
curl "http://localhost:8000/api/v1/colleges/1/news?search=robotics&page=1&limit=10"
```

## Service Methods

All endpoints use corresponding service methods from `CollegeService`:

```python
# In college_service.py
CollegeService.get_colleges()              # List colleges
CollegeService.get_college_data()          # Complete data
CollegeService.get_college_details()       # Details
CollegeService.get_college_ratings()       # Ratings
CollegeService.get_college_reviews()       # Reviews
CollegeService.get_fee_structure()         # Fees
CollegeService.get_placements()            # Placements
CollegeService.get_branch_placements()     # Branch placements
CollegeService.get_admissions()            # Admissions
CollegeService.get_academics()             # Academics
CollegeService.get_departments()           # Departments
CollegeService.get_infrastructure()        # Infrastructure
CollegeService.get_campus_experience()     # Campus life
CollegeService.get_clubs()                 # Clubs
CollegeService.get_events()                # Events
CollegeService.get_gallery()               # Gallery
CollegeService.get_alumni()                # Alumni
CollegeService.get_scholarships()          # Scholarships
CollegeService.get_news()                  # News
CollegeService.get_startups()              # Startups
CollegeService.get_social_media()          # Social media
CollegeService.get_nearby_places()         # Nearby places
```

## Response Format

All endpoints return:
```json
{
  "success": true,
  "message": "Operation completed successfully",
  "data": { /* endpoint-specific data */ }
}
```

## Common Query Parameters

| Parameter | Type | Used In | Description |
|-----------|------|---------|-------------|
| search | string | /colleges, /news | Search text (min 2 chars) |
| state | string | /colleges | Filter by state |
| type | string | /colleges | Filter by type |
| category | string | /colleges | Filter by category |
| sortBy | string | /colleges | Sort field |
| page | integer | /colleges, /news | Page number |
| limit | integer | /colleges, /news | Items per page |

## Implementation Pattern

Each endpoint follows this pattern:

```python
# 1. Route Handler (colleges.py)
@router.get("/{id}/endpoint")
def endpoint_name(id: int) -> BaseResponseSchema:
    data = CollegeService.service_method(id)
    return BaseResponseSchema(
        success=True,
        message="Success message",
        data=data
    )

# 2. Service Method (college_service.py)
@staticmethod
def service_method(college_id: int) -> dict:
    # Fetch from database
    # Transform data
    # Return formatted dict
    return data
```

## Frontend Integration

### JavaScript/TypeScript
```javascript
const API_BASE = 'http://localhost:8000/api/v1/colleges';

// Get college details
const details = await fetch(`${API_BASE}/1/details`).then(r => r.json());

// Get placements
const placements = await fetch(`${API_BASE}/1/placements`).then(r => r.json());

// Search colleges
const colleges = await fetch(`${API_BASE}?search=IIT&page=1`).then(r => r.json());
```

### React Hook Example
```javascript
import { useState, useEffect } from 'react';

function useCollegeDetails(collegeId) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetch(`http://localhost:8000/api/v1/colleges/${collegeId}/details`)
      .then(res => res.json())
      .then(json => {
        if (json.success) {
          setData(json.data);
        }
        setLoading(false);
      });
  }, [collegeId]);
  
  return { data, loading };
}
```

## Testing Commands

```bash
# Test all endpoints
curl http://localhost:8000/api/v1/colleges/1/details
curl http://localhost:8000/api/v1/colleges/1/ratings
curl http://localhost:8000/api/v1/colleges/1/reviews
curl http://localhost:8000/api/v1/colleges/1/fees
curl http://localhost:8000/api/v1/colleges/1/placements
curl http://localhost:8000/api/v1/colleges/1/placements/branches
curl http://localhost:8000/api/v1/colleges/1/admissions
curl http://localhost:8000/api/v1/colleges/1/academics
curl http://localhost:8000/api/v1/colleges/1/departments
curl http://localhost:8000/api/v1/colleges/1/infrastructure
curl http://localhost:8000/api/v1/colleges/1/campus-experience
curl http://localhost:8000/api/v1/colleges/1/clubs
curl http://localhost:8000/api/v1/colleges/1/events
curl http://localhost:8000/api/v1/colleges/1/gallery
curl http://localhost:8000/api/v1/colleges/1/alumni
curl http://localhost:8000/api/v1/colleges/1/scholarships
curl http://localhost:8000/api/v1/colleges/1/news
curl http://localhost:8000/api/v1/colleges/1/startups
curl http://localhost:8000/api/v1/colleges/1/social-media
curl http://localhost:8000/api/v1/colleges/1/nearby-places
```

## Common HTTP Status Codes

| Code | Meaning | When |
|------|---------|------|
| 200 | OK | Successful request |
| 400 | Bad Request | Invalid parameters |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Internal error |

## Next Steps

1. Replace dummy data with database queries
2. Add authentication for sensitive endpoints
3. Implement caching for frequently accessed data
4. Add rate limiting
5. Set up error logging and monitoring

## Documentation

For detailed documentation, see:
- [Full API Documentation](./COLLEGE_ENDPOINTS_API_DOCUMENTATION.md)
- OpenAPI/Swagger UI: http://localhost:8000/docs

---

**Last Updated**: October 29, 2025
