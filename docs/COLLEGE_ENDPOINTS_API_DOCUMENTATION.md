# College API Endpoints Documentation

## Table of Contents
1. [Overview](#overview)
2. [Base URL](#base-url)
3. [Authentication](#authentication)
4. [Response Structure](#response-structure)
5. [Endpoints](#endpoints)
   - [List Colleges](#1-list-colleges)
   - [Get Complete College Data](#2-get-complete-college-data)
   - [Get College Details](#3-get-college-details)
   - [Get College Ratings](#4-get-college-ratings)
   - [Get College Reviews](#5-get-college-reviews)
   - [Get Fee Structure](#6-get-fee-structure)
   - [Get Placements](#7-get-placements)
   - [Get Branch Placements](#8-get-branch-placements)
   - [Get Admissions](#9-get-admissions)
   - [Get Academics](#10-get-academics)
   - [Get Departments](#11-get-departments)
   - [Get Infrastructure](#12-get-infrastructure)
   - [Get Campus Experience](#13-get-campus-experience)
   - [Get Clubs](#14-get-clubs)
   - [Get Events](#15-get-events)
   - [Get Gallery](#16-get-gallery)
   - [Get Alumni](#17-get-alumni)
   - [Get Scholarships](#18-get-scholarships)
   - [Get News](#19-get-news)
   - [Get Startups](#20-get-startups)
   - [Get Social Media](#21-get-social-media)
   - [Get Nearby Places](#22-get-nearby-places)
6. [Implementation Guide](#implementation-guide)
7. [Error Handling](#error-handling)

---

## Overview

This document provides comprehensive documentation for all college-related API endpoints. Each endpoint returns structured data about colleges including their details, placements, infrastructure, campus life, and more.

---

## Base URL

```
Production: https://api.yourapp.com/api/v1/colleges
Development: http://localhost:8000/api/v1/colleges
```

---

## Authentication

Currently, these endpoints do not require authentication. For future implementation, add JWT tokens in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

---

## Response Structure

All endpoints return a standardized response format:

```json
{
  "success": true,
  "message": "Operation completed successfully",
  "data": {
    // Endpoint-specific data
  }
}
```

### Error Response

```json
{
  "success": false,
  "message": "Error message",
  "data": null
}
```

---

## Endpoints

### 1. List Colleges

**GET** `/`

Retrieve a paginated list of colleges with optional filtering and sorting.

#### Query Parameters

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| search | string | No | Search by college name (min 2 chars) | `IIT` |
| state | string | No | Filter by state | `Delhi` |
| type | string | No | Filter by type (Public/Private) | `Public` |
| category | string | No | Filter by category | `Engineering` |
| sortBy | string | No | Sort field (ranking/rating/fees/placement) | `rating` |
| page | integer | No | Page number (default: 1) | `1` |
| limit | integer | No | Items per page (max 100, default: 10) | `20` |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges?search=IIT&state=Delhi&type=Public&sortBy=rating&page=1&limit=10"
```

#### Response Example

```json
{
  "success": true,
  "message": "Colleges retrieved successfully",
  "data": {
    "colleges": [
      {
        "id": "1",
        "name": "Indian Institute of Technology Delhi",
        "shortName": "IIT Delhi",
        "location": "New Delhi",
        "state": "Delhi",
        "rating": 4.8,
        "reviews": 2453,
        "type": "Public",
        "category": "Engineering",
        "established": 1961,
        "fees": "₹2.5 Lakhs",
        "placement": "₹25 LPA",
        "ranking": 2,
        "featured": true,
        "courses": 42,
        "students": 8000,
        "image": "/api/placeholder/400/300"
      }
    ],
    "total": 15,
    "page": 1,
    "size": 10
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_colleges()`
2. **Database Query**: Filter colleges based on query parameters
3. **Sorting**: Apply sorting if sortBy parameter is provided
4. **Pagination**: Calculate offset and limit for pagination
5. **Format Response**: Convert numeric values to display format

---

### 2. Get Complete College Data

**GET** `/{id}`

Retrieve all comprehensive data for a specific college in a single API call.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1"
```

#### Response Example

```json
{
  "success": true,
  "message": "College retrieved successfully",
  "data": {
    "college_details": { /* ... */ },
    "college_placements": { /* ... */ },
    "college_branch_placements": { /* ... */ },
    "college_departments": { /* ... */ },
    "college_infrastructure": { /* ... */ },
    "college_campus_experience": { /* ... */ },
    "college_clubs": { /* ... */ },
    "college_events": { /* ... */ },
    "college_gallery": { /* ... */ },
    "college_alumni": { /* ... */ },
    "college_scholarships": { /* ... */ },
    "college_startups": { /* ... */ },
    "college_social_media": { /* ... */ },
    "college_nearby_places": { /* ... */ },
    "college_admissions": { /* ... */ },
    "college_academics": { /* ... */ },
    "college_fee_structure": { /* ... */ }
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_college_data()`
2. **Aggregate Data**: Call all individual service methods
3. **Combine Results**: Merge all data into a single response
4. **Error Handling**: Return 404 if college not found

---

### 3. Get College Details

**GET** `/{id}/details`

Retrieve basic college information including location, contact, and about section.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/details"
```

#### Response Example

```json
{
  "success": true,
  "message": "College details retrieved successfully",
  "data": {
    "id": 1,
    "name": "National Institute of Technology Alpha",
    "shortName": "NITA",
    "aboutHTML": "<p>National Institute of Technology Alpha (NITA) is a premier engineering institute...</p>",
    "established": 1965,
    "type": "Public",
    "category": "Engineering",
    "location": {
      "address": "Sector 22, Academic Road",
      "city": "Dadri",
      "state": "Uttar Pradesh",
      "pincode": "203207",
      "coordinates": {
        "lat": 28.567,
        "lng": 77.553
      }
    },
    "contact": {
      "phone": ["+91-120-1234567", "+91-120-7654321"],
      "email": ["info@nita.edu.in", "admissions@nita.edu.in"],
      "website": "https://www.nita.edu.in",
      "admissionHelpline": "+91-120-1112223"
    }
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_college_details()`
2. **Database Query**: Fetch college basic information by ID
3. **Include Relations**: Load location and contact information
4. **Format HTML**: Ensure aboutHTML is properly formatted

---

### 4. Get College Ratings

**GET** `/{id}/ratings`

Retrieve overall and category-wise ratings for a college.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/ratings"
```

#### Response Example

```json
{
  "success": true,
  "message": "College ratings retrieved successfully",
  "data": {
    "overall": 4.3,
    "academics": 4.5,
    "infrastructure": 4.1,
    "faculty": 4.4,
    "placement": 4.2,
    "hostelLife": 3.9,
    "socialLife": 4.0,
    "totalReviews": 1287
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_college_ratings()`
2. **Calculate Ratings**: Aggregate ratings from reviews table
3. **Category Average**: Calculate average for each category
4. **Overall Rating**: Calculate weighted average of all categories
5. **Count Reviews**: Count total number of reviews

---

### 5. Get College Reviews

**GET** `/{id}/reviews`

Retrieve student reviews, testimonials, and rating distribution.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/reviews"
```

#### Response Example

```json
{
  "success": true,
  "message": "College reviews retrieved successfully",
  "data": {
    "highlights": [
      "Supportive faculty and research culture",
      "Good placements for CS and ECE",
      "Hostel facilities improving"
    ],
    "distribution": [
      {"label": "5-star", "value": 46},
      {"label": "4-star", "value": 32},
      {"label": "3-star", "value": 15},
      {"label": "2-star", "value": 5},
      {"label": "1-star", "value": 2}
    ],
    "testimonials": [
      {
        "id": "rv1",
        "name": "Neha Gupta",
        "program": "B.Tech CSE",
        "batch": "2024",
        "content": "Great exposure to coding competitions and projects.",
        "rating": 5
      }
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_college_reviews()`
2. **Fetch Reviews**: Get recent reviews from database
3. **Calculate Distribution**: Count reviews per star rating
4. **Extract Highlights**: Use NLP or manual curation for highlights
5. **Format Testimonials**: Include student details and content

---

### 6. Get Fee Structure

**GET** `/{id}/fees`

Retrieve detailed fee structure for all programs.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/fees"
```

#### Response Example

```json
{
  "success": true,
  "message": "College fee structure retrieved successfully",
  "data": {
    "undergraduate": {
      "B.Tech": {
        "tuition": "INR 1,20,000 per year",
        "mess": "INR 60,000 per year",
        "hostel": "INR 45,000 per year",
        "other": "INR 15,500 per year",
        "total": "INR 1,80,500 per year"
      }
    },
    "postgraduate": {
      "M.Tech": {
        "tuition": "INR 1,50,000 per year",
        "hostel": "INR 50,000 per year",
        "other": "INR 20,000 per year",
        "total": "INR 2,20,000 per year"
      },
      "MBA": {
        "tuition": "INR 2,00,000 per year",
        "hostel": "INR 60,000 per year",
        "other": "INR 25,000 per year",
        "total": "INR 2,85,000 per year"
      }
    },
    "phd": {
      "tuition": "INR 50,000 per year",
      "hostel": "INR 30,000 per year",
      "other": "INR 10,000 per year",
      "total": "INR 90,000 per year"
    }
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_fee_structure()`
2. **Fetch Fee Data**: Query fees table with program mapping
3. **Group by Level**: Organize by undergraduate, postgraduate, PhD
4. **Calculate Totals**: Sum all fee components
5. **Format Currency**: Display in readable format (INR)

---

### 7. Get Placements

**GET** `/{id}/placements`

Retrieve comprehensive placement statistics including packages, trends, and success stories.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/placements"
```

#### Response Example

```json
{
  "success": true,
  "message": "College placement data retrieved successfully",
  "data": {
    "averagePackage": "INR 10.8 LPA",
    "highestPackage": "INR 52 LPA",
    "placementRate": 86,
    "medianPackage": "INR 9.5 LPA",
    "topRecruiters": ["Google", "Microsoft", "TCS", "Infosys", "Amazon", "Accenture"],
    "internationalOffers": 7,
    "salaryTrends": [
      {
        "year": 2021,
        "average": "INR 8.7 LPA",
        "highest": "INR 32 LPA",
        "placementRate": 82
      }
    ],
    "sectorDistribution": [
      {"sector": "IT/Software", "percentage": 52}
    ],
    "internshipStats": {
      "totalInternships": 356,
      "ppoRate": 18,
      "globalInternships": 12,
      "averageStipend": "INR 35,000 per month"
    },
    "successStories": [
      {
        "name": "Riya Sharma",
        "company": "Google",
        "package": "INR 48 LPA",
        "role": "Software Engineer",
        "story": "Riya contributed to open-source projects..."
      }
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_placements()`
2. **Aggregate Statistics**: Calculate average, median, highest packages
3. **Trend Analysis**: Group placements by year for trends
4. **Sector Distribution**: Calculate percentage per sector
5. **Success Stories**: Fetch featured alumni placement stories
6. **Internship Data**: Include internship statistics

---

### 8. Get Branch Placements

**GET** `/{id}/placements/branches`

Retrieve branch-wise placement statistics.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/placements/branches"
```

#### Response Example

```json
{
  "success": true,
  "message": "College branch-wise placement data retrieved successfully",
  "data": {
    "branches": [
      {
        "name": "Computer Science and Engineering",
        "averagePackage": "INR 12.6 LPA",
        "medianPackage": "INR 11.2 LPA",
        "highestPackage": "INR 52 LPA",
        "placementRate": 95,
        "offers": 176,
        "topRoles": ["Software Engineer", "SDE", "Data Engineer"],
        "recruiters": ["Google", "Amazon", "Microsoft", "Flipkart"]
      }
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_branch_placements()`
2. **Group by Branch**: Aggregate placement data per branch
3. **Calculate Statistics**: Compute average, median, highest per branch
4. **Top Roles**: Identify most common job roles
5. **Top Recruiters**: List companies hiring from each branch

---

### 9. Get Admissions

**GET** `/{id}/admissions`

Retrieve admission information including dates, eligibility, and documents.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/admissions"
```

#### Response Example

```json
{
  "success": true,
  "message": "College admission information retrieved successfully",
  "data": {
    "overview": "Admissions are based on merit and entrance exams...",
    "programs": {
      "B.Tech": {
        "importantDates": [
          {
            "event": "Application Start",
            "startDate": "2025-02-15",
            "endDate": "2025-04-30",
            "status": "Closed"
          }
        ],
        "eligibility": ["Class 12 with PCM", "JEE Main score", "Minimum 75% aggregate"],
        "requiredDocuments": ["Photo ID", "Class 12 Marksheet"],
        "suggestions": ["Prepare for JEE Main with mock tests."]
      }
    },
    "generalGuidelines": [
      "Ensure all documents are uploaded in the correct format."
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_admissions()`
2. **Program-wise Data**: Organize by program (B.Tech, M.Tech, etc.)
3. **Timeline Management**: Track important dates and statuses
4. **Eligibility Rules**: Define criteria for each program
5. **Document Checklist**: List required documents
6. **Status Updates**: Mark dates as Open/Closed/Upcoming

---

### 10. Get Academics

**GET** `/{id}/academics`

Retrieve academic information including courses and faculty ratios.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/academics"
```

#### Response Example

```json
{
  "success": true,
  "message": "College academic information retrieved successfully",
  "data": {
    "courses": {
      "undergraduate": ["B.Tech CSE", "B.Tech ECE", "B.Tech ME"],
      "postgraduate": ["M.Tech CSE", "M.Tech VLSI", "MBA"],
      "phd": ["Computer Science", "Electronics", "Mechanical"]
    },
    "facultyCount": 212,
    "studentFacultyRatio": "1:15"
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_academics()`
2. **Course Listing**: Group courses by level
3. **Faculty Count**: Query total faculty members
4. **Calculate Ratio**: Compute student-faculty ratio
5. **Format Display**: Present in readable format

---

### 11. Get Departments

**GET** `/{id}/departments`

Retrieve detailed department information including faculty and courses.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/departments"
```

#### Response Example

```json
{
  "success": true,
  "message": "College departments retrieved successfully",
  "data": {
    "departments": [
      {
        "id": "cse",
        "name": "Computer Science and Engineering",
        "summary": "Focus on algorithms, systems, AI/ML...",
        "strengths": ["Competitive programming culture", "Strong research output"],
        "undergraduateCourses": ["Data Structures", "Operating Systems"],
        "postgraduateCourses": ["Advanced Algorithms", "Distributed Systems"],
        "phdCourses": ["Research Methodology in CS"],
        "faculty": [
          {
            "name": "Dr. Alice Smith",
            "image": "https://picsum.photos/seed/alice/400/400",
            "designation": "Professor",
            "researchInterests": ["Machine Learning", "Data Mining"]
          }
        ]
      }
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_departments()`
2. **Department Listing**: Fetch all departments
3. **Course Mapping**: Link courses to departments
4. **Faculty Association**: Include faculty members per department
5. **Research Areas**: List department strengths and focus areas

---

### 12. Get Infrastructure

**GET** `/{id}/infrastructure`

Retrieve infrastructure details including campus, facilities, and hostels.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/infrastructure"
```

#### Response Example

```json
{
  "success": true,
  "message": "College infrastructure retrieved successfully",
  "data": {
    "overview": "A 300-acre green campus...",
    "keyHighlights": ["Central library with 1.2 lakh volumes"],
    "campus": {
      "area": "300 acres",
      "buildings": 28,
      "labs": 64,
      "libraries": 3
    },
    "facilities": ["Auditorium", "Seminar Halls", "Innovation Lab"],
    "hostels": [
      {
        "name": "Aryabhatta Hostel",
        "capacity": 1200,
        "rooms": "Double occupancy, AC/Non-AC options",
        "facilities": ["Laundry", "Common rooms", "Mess"],
        "gallery": ["https://picsum.photos/seed/hostel1/800/400"],
        "description": "One of the largest hostels...",
        "reviews": [
          {
            "student": "Karan Mehta",
            "batch": "2023",
            "comment": "Spacious rooms"
          }
        ]
      }
    ],
    "innovationCenters": [
      {
        "name": "Center for AI and Robotics",
        "focus": "Applied AI, robotics",
        "description": "Supports student projects...",
        "link": "https://www.nita.edu.in/ai-center",
        "gallery": ["https://picsum.photos/seed/ai1/800/400"]
      }
    ],
    "digitalInfrastructure": ["25 Gbps backbone", "Smart classrooms"],
    "sustainabilityInitiatives": [
      {
        "title": "Solar PV across hostels",
        "impact": "Cuts 20% grid usage"
      }
    ],
    "transport": [
      {
        "mode": "Campus shuttle",
        "frequency": "Every 15 minutes"
      }
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_infrastructure()`
2. **Campus Data**: Fetch campus area, buildings count
3. **Facilities List**: Query available facilities
4. **Hostel Details**: Include capacity, amenities, reviews
5. **Innovation Centers**: List research and innovation labs
6. **Sustainability**: Highlight green initiatives
7. **Transport**: List transportation options

---

### 13. Get Campus Experience

**GET** `/{id}/campus-experience`

Retrieve campus life information including dining, sports, and wellness programs.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/campus-experience"
```

#### Response Example

```json
{
  "success": true,
  "message": "College campus experience retrieved successfully",
  "data": {
    "lifestyleHighlights": [
      {
        "title": "Festive campus",
        "description": "Annual tech, cultural, and sports fests..."
      }
    ],
    "supportServices": [
      {
        "name": "Counseling Center",
        "description": "Mental health support and mentoring."
      }
    ],
    "diningOptions": [
      {
        "name": "Central Mess",
        "type": "Veg/Non-veg",
        "signature": "Thali, biryani",
        "openTill": "22:00"
      }
    ],
    "sportsAndFitness": [
      {
        "name": "Indoor stadium",
        "details": "Badminton, table tennis"
      }
    ],
    "wellnessPrograms": [
      {
        "name": "Mindful Mondays",
        "description": "Guided meditation and stress relief."
      }
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_campus_experience()`
2. **Lifestyle Data**: Describe campus culture
3. **Support Services**: List counseling, career services
4. **Dining Options**: Include mess, cafeterias, timings
5. **Sports Facilities**: List sports and fitness options
6. **Wellness Programs**: Include mental health initiatives

---

### 14. Get Clubs

**GET** `/{id}/clubs`

Retrieve student clubs and societies information.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/clubs"
```

#### Response Example

```json
{
  "success": true,
  "message": "College clubs retrieved successfully",
  "data": {
    "clubs": [
      {
        "id": "coding",
        "name": "Coding Club",
        "description": "Competitive programming, hackathons...",
        "achievements": ["ICPC Regionals top 10", "Google Summer of Code selections"],
        "contactEmail": "coding.club@nita.edu.in",
        "social": {
          "instagram": "https://instagram.com/nita_coding",
          "youtube": "https://youtube.com/@nita_coding",
          "linkedin": "https://linkedin.com/company/nita-coding"
        },
        "mediaEmbed": "<iframe src='https://www.youtube.com/embed/...' />"
      }
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_clubs()`
2. **Club Listing**: Fetch all active clubs
3. **Achievements**: Include notable accomplishments
4. **Contact Info**: Provide email and social media links
5. **Media Content**: Embed videos or presentations

---

### 15. Get Events

**GET** `/{id}/events`

Retrieve upcoming and past college events.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/events"
```

#### Response Example

```json
{
  "success": true,
  "message": "College events retrieved successfully",
  "data": {
    "events": [
      {
        "id": "techfest25",
        "name": "TechFest 2025",
        "type": "Technical",
        "description": "Workshops, coding contests...",
        "date": "2025-11-15",
        "image": "https://picsum.photos/seed/techfest/800/400",
        "location": "Main Auditorium",
        "registrationLink": "https://www.nita.edu.in/techfest",
        "highlights": ["Keynote by industry leader", "24h hackathon"],
        "social": {
          "instagram": "https://instagram.com/nita_techfest",
          "website": "https://www.nita.edu.in/techfest"
        },
        "mediaEmbed": "<iframe src='https://player.vimeo.com/video/...' />"
      }
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_events()`
2. **Event Listing**: Fetch upcoming and recent events
3. **Event Types**: Categorize (Technical, Cultural, Sports)
4. **Registration**: Include registration links
5. **Event Details**: Date, location, highlights
6. **Media**: Images and embedded content

---

### 16. Get Gallery

**GET** `/{id}/gallery`

Retrieve college photo gallery organized by categories.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/gallery"
```

#### Response Example

```json
{
  "success": true,
  "message": "College gallery images retrieved successfully",
  "data": {
    "images": {
      "campus": [
        {
          "description": "Aerial view of NITA campus",
          "url": "https://picsum.photos/seed/campus1/1200/800",
          "date": "2024-10-10"
        }
      ],
      "hostel": [
        {
          "description": "Aryabhatta Hostel exterior",
          "url": "https://picsum.photos/seed/hostel1/1200/800",
          "date": "2024-10-11"
        }
      ],
      "facilities": [
        {
          "description": "Central Library reading hall",
          "url": "https://picsum.photos/seed/library/1200/800",
          "date": "2024-10-11"
        }
      ],
      "events": [
        {
          "description": "TechFest 2024 hackathon",
          "url": "https://picsum.photos/seed/event1/1200/800",
          "date": "2024-10-12"
        }
      ]
    }
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_gallery()`
2. **Organize by Category**: Group images (campus, hostel, facilities, events)
3. **Image Metadata**: Include description, date
4. **Image Optimization**: Use CDN for fast loading
5. **Lazy Loading**: Implement for better performance

---

### 17. Get Alumni

**GET** `/{id}/alumni`

Retrieve alumni network information.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/alumni"
```

#### Response Example

```json
{
  "success": true,
  "message": "College alumni network retrieved successfully",
  "data": {
    "totalAlumni": 18500,
    "notableAlumni": [
      {
        "id": "al1",
        "name": "Anita Verma",
        "batch": "2010",
        "position": "VP Engineering",
        "company": "TCS",
        "image": "https://picsum.photos/seed/al1/400/400"
      }
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_alumni()`
2. **Count Total**: Query total alumni count
3. **Notable Alumni**: Feature successful alumni
4. **Profile Data**: Include current position, company
5. **Images**: Add professional photos

---

### 18. Get Scholarships

**GET** `/{id}/scholarships`

Retrieve available scholarships information.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/scholarships"
```

#### Response Example

```json
{
  "success": true,
  "message": "College scholarships retrieved successfully",
  "data": {
    "scholarships": [
      {
        "id": "sch1",
        "name": "Merit Scholarship",
        "amount": "INR 50,000",
        "eligibility": "Top 10% in entrance",
        "description": "Awarded to high-performing entrants."
      }
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_scholarships()`
2. **List Scholarships**: Fetch all available scholarships
3. **Eligibility Criteria**: Define clear criteria
4. **Amount Details**: Specify scholarship amount
5. **Application Info**: Link to application process

---

### 19. Get News

**GET** `/{id}/news`

Retrieve college news with optional search and pagination.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search in title or content (min 2 chars) |
| page | integer | No | Page number (default: 1) |
| limit | integer | No | Items per page (max 50, default: 10) |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/news?search=robotics&page=1&limit=10"
```

#### Response Example

```json
{
  "success": true,
  "message": "College news retrieved successfully",
  "data": {
    "items": [
      {
        "id": "n1",
        "title": "NITA hosts National Robotics Championship",
        "date": "2025-10-15",
        "category": "Events",
        "excerpt": "Students from 50+ colleges compete",
        "image": "https://picsum.photos/seed/news1/800/400"
      }
    ],
    "total": 5,
    "page": 1,
    "limit": 10
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_news()`
2. **Search Functionality**: Filter by title or content
3. **Pagination**: Implement offset-based pagination
4. **Sort by Date**: Show latest news first
5. **Category Tags**: Organize by news type

---

### 20. Get Startups

**GET** `/{id}/startups`

Retrieve student startups information.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/startups"
```

#### Response Example

```json
{
  "success": true,
  "message": "College startups retrieved successfully",
  "data": {
    "startups": [
      {
        "id": "st1",
        "name": "EduTech Pro",
        "founder": "Rahul Sharma (2020 batch)",
        "description": "AI-powered learning platform",
        "funding": "$2M Series A",
        "image": "https://picsum.photos/seed/startup1/400/400"
      }
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_startups()`
2. **List Startups**: Fetch student-founded companies
3. **Founder Info**: Include batch and name
4. **Funding Details**: Show funding rounds
5. **Success Metrics**: Add growth indicators

---

### 21. Get Social Media

**GET** `/{id}/social-media`

Retrieve college official social media links.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/social-media"
```

#### Response Example

```json
{
  "success": true,
  "message": "College social media links retrieved successfully",
  "data": {
    "official": {
      "facebook": "https://facebook.com/nita.official",
      "twitter": "https://twitter.com/nita_official",
      "instagram": "https://instagram.com/nita.official",
      "youtube": "https://youtube.com/@nita_official",
      "linkedin": "https://linkedin.com/school/nita"
    }
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_social_media()`
2. **Platform Links**: Store links for major platforms
3. **Verification**: Ensure links are active
4. **Update Mechanism**: Regular verification process

---

### 22. Get Nearby Places

**GET** `/{id}/nearby-places`

Retrieve nearby places of interest.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | College ID |

#### Request Example

```bash
curl -X GET "http://localhost:8000/api/v1/colleges/1/nearby-places"
```

#### Response Example

```json
{
  "success": true,
  "message": "College nearby places retrieved successfully",
  "data": {
    "places": [
      {
        "id": "p1",
        "name": "Metro Station",
        "distance": "2 km",
        "type": "Transport"
      },
      {
        "id": "p2",
        "name": "City Mall",
        "distance": "3.5 km",
        "type": "Shopping"
      }
    ]
  }
}
```

#### Implementation Steps

1. **Service Method**: `CollegeService.get_nearby_places()`
2. **Location Data**: Use college coordinates
3. **Category Types**: Group by type (Transport, Shopping, Healthcare)
4. **Distance Calculation**: Calculate from college location
5. **POI Integration**: Use Google Places API or similar

---

## Implementation Guide

### Backend Architecture

```
app/
├── api/
│   └── v1/
│       └── endpoints/
│           └── colleges.py          # API route handlers
├── services/
│   └── college_service.py           # Business logic
├── models/
│   └── college.py                   # Database models
└── schemas/
    ├── college.py                   # Pydantic schemas
    └── base.py                      # Base response schema
```

### Service Layer Pattern

Each endpoint follows this pattern:

```python
# 1. API Endpoint (colleges.py)
@router.get("/{id}/details")
def get_college_details(id: int) -> BaseResponseSchema:
    # Call service method
    data = CollegeService.get_college_details(id)
    
    # Return standardized response
    return BaseResponseSchema(
        success=True,
        message="College details retrieved successfully",
        data=data
    )

# 2. Service Method (college_service.py)
@staticmethod
def get_college_details(college_id: int) -> dict:
    # Business logic
    # Database queries
    # Data transformation
    return formatted_data
```

### Database Schema Recommendations

```sql
-- Colleges table
CREATE TABLE colleges (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    short_name VARCHAR(50),
    about_html TEXT,
    established INTEGER,
    type VARCHAR(50),
    category VARCHAR(50),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- College locations
CREATE TABLE college_locations (
    id INTEGER PRIMARY KEY,
    college_id INTEGER REFERENCES colleges(id),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    pincode VARCHAR(10),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8)
);

-- College contacts
CREATE TABLE college_contacts (
    id INTEGER PRIMARY KEY,
    college_id INTEGER REFERENCES colleges(id),
    phone_numbers JSON,
    emails JSON,
    website VARCHAR(255),
    admission_helpline VARCHAR(50)
);

-- Placements
CREATE TABLE placements (
    id INTEGER PRIMARY KEY,
    college_id INTEGER REFERENCES colleges(id),
    year INTEGER,
    average_package DECIMAL(10, 2),
    highest_package DECIMAL(10, 2),
    median_package DECIMAL(10, 2),
    placement_rate DECIMAL(5, 2)
);

-- Reviews
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    college_id INTEGER REFERENCES colleges(id),
    student_name VARCHAR(100),
    batch VARCHAR(20),
    rating INTEGER,
    comment TEXT,
    category VARCHAR(50),
    created_at TIMESTAMP
);

-- Add more tables as needed...
```

### Frontend Integration Examples

#### React/Next.js

```javascript
// API Client
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1';

export const collegeAPI = {
  // Get list of colleges
  getColleges: async (params) => {
    const response = await axios.get(`${API_BASE_URL}/colleges`, { params });
    return response.data;
  },
  
  // Get college details
  getCollegeDetails: async (id) => {
    const response = await axios.get(`${API_BASE_URL}/colleges/${id}/details`);
    return response.data;
  },
  
  // Get placements
  getPlacements: async (id) => {
    const response = await axios.get(`${API_BASE_URL}/colleges/${id}/placements`);
    return response.data;
  },
  
  // Add more methods for other endpoints...
};

// Usage in component
import { useEffect, useState } from 'react';
import { collegeAPI } from './api/college';

function CollegeDetails({ collegeId }) {
  const [details, setDetails] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    const fetchDetails = async () => {
      try {
        const response = await collegeAPI.getCollegeDetails(collegeId);
        if (response.success) {
          setDetails(response.data);
        }
      } catch (error) {
        console.error('Error fetching college details:', error);
      } finally {
        setLoading(false);
      }
    };
    
    fetchDetails();
  }, [collegeId]);
  
  if (loading) return <div>Loading...</div>;
  
  return (
    <div>
      <h1>{details.name}</h1>
      <p>{details.aboutHTML}</p>
      {/* Render more details */}
    </div>
  );
}
```

#### TypeScript Interfaces

```typescript
// types/college.ts
export interface CollegeDetails {
  id: number;
  name: string;
  aboutHTML: string;
  shortName: string;
  established: number;
  type: 'Public' | 'Private' | 'Deemed';
  category: 'Engineering' | 'Medical' | 'Management';
  location: {
    address: string;
    city: string;
    state: string;
    pincode: string;
    coordinates: { lat: number; lng: number };
  };
  contact: {
    phone: string[];
    email: string[];
    website: string;
    admissionHelpline: string;
  };
}

export interface CollegeRatings {
  overall: number;
  academics: number;
  infrastructure: number;
  faculty: number;
  placement: number;
  hostelLife: number;
  socialLife: number;
  totalReviews: number;
}

// Add more interfaces for other endpoints...
```

---

## Error Handling

### Common HTTP Status Codes

| Status Code | Meaning | When to Use |
|-------------|---------|-------------|
| 200 | OK | Successful request |
| 400 | Bad Request | Invalid parameters |
| 404 | Not Found | College ID doesn't exist |
| 500 | Internal Server Error | Server-side error |

### Error Response Format

```json
{
  "success": false,
  "message": "College not found",
  "data": null
}
```

### Error Handling in Service Layer

```python
from fastapi import HTTPException, status

@staticmethod
def get_college_details(college_id: int) -> dict:
    try:
        # Fetch college from database
        college = database.get_college(college_id)
        
        if not college:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"College with ID {college_id} not found"
            )
        
        return format_college_details(college)
        
    except HTTPException:
        raise  # Re-raise HTTP exceptions
        
    except Exception as e:
        # Log the error
        logger.error(f"Error fetching college {college_id}: {str(e)}")
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching college details"
        )
```

---

## Best Practices

### 1. Caching Strategy

```python
from functools import lru_cache
from redis import Redis

# In-memory cache for frequently accessed data
@lru_cache(maxsize=100)
def get_college_details_cached(college_id: int):
    return CollegeService.get_college_details(college_id)

# Redis cache for distributed systems
redis_client = Redis(host='localhost', port=6379, db=0)

def get_with_cache(key, fetch_func, expiry=3600):
    cached = redis_client.get(key)
    if cached:
        return json.loads(cached)
    
    data = fetch_func()
    redis_client.setex(key, expiry, json.dumps(data))
    return data
```

### 2. Rate Limiting

```python
from fastapi_limiter.depends import RateLimiter

@router.get("/{id}/details", dependencies=[Depends(RateLimiter(times=100, seconds=60))])
def get_college_details(id: int):
    # Limit to 100 requests per minute
    pass
```

### 3. Pagination Best Practices

```python
# Always include pagination metadata
{
  "data": [...],
  "pagination": {
    "total": 150,
    "page": 1,
    "pageSize": 10,
    "totalPages": 15,
    "hasNext": true,
    "hasPrev": false
  }
}
```

### 4. API Versioning

```python
# Include version in URL
/api/v1/colleges/
/api/v2/colleges/

# Or in headers
headers = {
    "Accept": "application/vnd.api+json; version=1"
}
```

### 5. Documentation

- Use OpenAPI/Swagger for automatic documentation
- Include request/response examples
- Document error scenarios
- Keep this guide updated

---

## Testing

### Unit Tests

```python
import pytest
from app.services.college_service import CollegeService

def test_get_college_details():
    college_id = 1
    details = CollegeService.get_college_details(college_id)
    
    assert details is not None
    assert details['id'] == college_id
    assert 'name' in details
    assert 'location' in details

def test_get_placements():
    college_id = 1
    placements = CollegeService.get_placements(college_id)
    
    assert 'averagePackage' in placements
    assert 'highestPackage' in placements
    assert placements['placementRate'] >= 0
    assert placements['placementRate'] <= 100
```

### Integration Tests

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_college_details_endpoint():
    response = client.get("/api/v1/colleges/1/details")
    
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert 'data' in response.json()

def test_college_not_found():
    response = client.get("/api/v1/colleges/99999/details")
    
    assert response.status_code == 404
```

---

## Performance Optimization

### 1. Database Indexes

```sql
-- Create indexes on frequently queried fields
CREATE INDEX idx_colleges_state ON colleges(state);
CREATE INDEX idx_colleges_type ON colleges(type);
CREATE INDEX idx_colleges_category ON colleges(category);
CREATE INDEX idx_placements_college_year ON placements(college_id, year);
```

### 2. Query Optimization

```python
# Use select_related for foreign keys
colleges = College.objects.select_related('location', 'contact').all()

# Use prefetch_related for many-to-many
colleges = College.objects.prefetch_related('departments', 'clubs').all()

# Only fetch needed fields
colleges = College.objects.only('id', 'name', 'rating').all()
```

### 3. Response Compression

```python
from fastapi.middleware.gzip import GZipMiddleware

app.add_middleware(GZipMiddleware, minimum_size=1000)
```

---

## Monitoring and Logging

```python
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Log API requests
@router.get("/{id}/details")
def get_college_details(id: int):
    start_time = datetime.now()
    
    try:
        logger.info(f"Fetching details for college {id}")
        data = CollegeService.get_college_details(id)
        
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(f"Successfully fetched college {id} in {duration}s")
        
        return BaseResponseSchema(success=True, data=data)
        
    except Exception as e:
        logger.error(f"Error fetching college {id}: {str(e)}")
        raise
```

---

## Security Considerations

1. **Input Validation**: Validate all input parameters
2. **SQL Injection Prevention**: Use parameterized queries
3. **Rate Limiting**: Prevent abuse
4. **Authentication**: Add JWT for sensitive endpoints
5. **CORS**: Configure allowed origins
6. **HTTPS**: Use SSL/TLS in production
7. **Sanitize HTML**: Clean user-generated HTML content

---

## Deployment Checklist

- [ ] Database migrations completed
- [ ] Environment variables configured
- [ ] API documentation deployed
- [ ] Rate limiting configured
- [ ] Caching layer implemented
- [ ] Logging and monitoring set up
- [ ] Error tracking configured (Sentry, etc.)
- [ ] Load testing completed
- [ ] Security audit passed
- [ ] Backup strategy in place

---

## Support and Contact

For questions or issues:
- GitHub Issues: [repository link]
- Email: dev@yourapp.com
- Slack: #api-support

---

**Last Updated**: October 29, 2025  
**Version**: 1.0.0  
**Maintained By**: Development Team
