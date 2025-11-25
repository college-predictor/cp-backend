from app.models.college import College
from app.schemas.college import CollegeListPageResponse
from typing import Optional, List, Tuple
import re

class CollegeService:
    @staticmethod
    async def get_colleges(
        query: dict = {},
        sort_criteria: Optional[List[Tuple[str, int]]] = None,
        page: int = 1,
        page_size: int = 10
    ) -> CollegeListPageResponse:
        # Sample colleges data
        all_colleges = [
            {
                "id": "1",
                "name": 'Indian Institute of Technology Delhi',
                "shortName": 'IIT Delhi',
                "location": 'New Delhi',
                "state": 'Delhi',
                "rating": 4.8,
                "reviews": 2453,
                "type": 'Public',
                "category": 'Engineering',
                "established": 1961,
                "fees": 250000,
                "placement": 2500000,
                "ranking": 2,
                "featured": True,
                "courses": 42,
                "students": 8000,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "2",
                "name": 'All India Institute of Medical Sciences',
                "shortName": 'AIIMS Delhi',
                "location": 'New Delhi',
                "state": 'Delhi',
                "rating": 4.9,
                "reviews": 1876,
                "type": 'Public',
                "category": 'Medical',
                "established": 1956,
                "fees": 150000,
                "placement": 3000000,
                "ranking": 1,
                "featured": True,
                "courses": 28,
                "students": 3000,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "3",
                "name": 'Indian Institute of Management Ahmedabad',
                "shortName": 'IIM Ahmedabad',
                "location": 'Ahmedabad',
                "state": 'Gujarat',
                "rating": 4.7,
                "reviews": 1234,
                "type": 'Public',
                "category": 'Management',
                "established": 1961,
                "fees": 2500000,
                "placement": 3500000,
                "ranking": 1,
                "featured": True,
                "courses": 15,
                "students": 1200,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "4",
                "name": 'Indian Institute of Science',
                "shortName": 'IISc Bangalore',
                "location": 'Bangalore',
                "state": 'Karnataka',
                "rating": 4.8,
                "reviews": 987,
                "type": 'Public',
                "category": 'Science & Research',
                "established": 1909,
                "fees": 200000,
                "placement": 2800000,
                "ranking": 1,
                "featured": True,
                "courses": 35,
                "students": 4500,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "5",
                "name": 'Delhi University',
                "shortName": 'DU',
                "location": 'New Delhi',
                "state": 'Delhi',
                "rating": 4.5,
                "reviews": 5432,
                "type": 'Public',
                "category": 'Arts & Science',
                "established": 1922,
                "fees": 50000,
                "placement": 800000,
                "ranking": 12,
                "featured": False,
                "courses": 180,
                "students": 400000,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "6",
                "name": 'Indian Institute of Technology Bombay',
                "shortName": 'IIT Bombay',
                "location": 'Mumbai',
                "state": 'Maharashtra',
                "rating": 4.8,
                "reviews": 2156,
                "type": 'Public',
                "category": 'Engineering',
                "established": 1958,
                "fees": 250000,
                "placement": 2700000,
                "ranking": 3,
                "featured": True,
                "courses": 45,
                "students": 9000,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "7",
                "name": 'Jawaharlal Nehru University',
                "shortName": 'JNU',
                "location": 'New Delhi',
                "state": 'Delhi',
                "rating": 4.6,
                "reviews": 1543,
                "type": 'Public',
                "category": 'Arts & Science',
                "established": 1969,
                "fees": 20000,
                "placement": 600000,
                "ranking": 8,
                "featured": False,
                "courses": 75,
                "students": 8500,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "8",
                "name": 'Indian Institute of Technology Madras',
                "shortName": 'IIT Madras',
                "location": 'Chennai',
                "state": 'Tamil Nadu',
                "rating": 4.9,
                "reviews": 2891,
                "type": 'Public',
                "category": 'Engineering',
                "established": 1959,
                "fees": 250000,
                "placement": 2800000,
                "ranking": 1,
                "featured": True,
                "courses": 50,
                "students": 10000,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "9",
                "name": 'National Law School of India University',
                "shortName": 'NLSIU Bangalore',
                "location": 'Bangalore',
                "state": 'Karnataka',
                "rating": 4.7,
                "reviews": 876,
                "type": 'Public',
                "category": 'Law',
                "established": 1987,
                "fees": 400000,
                "placement": 2000000,
                "ranking": 1,
                "featured": True,
                "courses": 8,
                "students": 800,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "10",
                "name": 'Banaras Hindu University',
                "shortName": 'BHU',
                "location": 'Varanasi',
                "state": 'Uttar Pradesh',
                "rating": 4.4,
                "reviews": 3421,
                "type": 'Public',
                "category": 'Arts & Science',
                "established": 1916,
                "fees": 60000,
                "placement": 700000,
                "ranking": 15,
                "featured": False,
                "courses": 140,
                "students": 30000,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "11",
                "name": 'BITS Pilani',
                "shortName": 'BITS Pilani',
                "location": 'Pilani',
                "state": 'Rajasthan',
                "rating": 4.6,
                "reviews": 1987,
                "type": 'Private',
                "category": 'Engineering',
                "established": 1964,
                "fees": 450000,
                "placement": 2300000,
                "ranking": 5,
                "featured": True,
                "courses": 38,
                "students": 4500,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "12",
                "name": 'Manipal Academy of Higher Education',
                "shortName": 'MAHE',
                "location": 'Manipal',
                "state": 'Karnataka',
                "rating": 4.3,
                "reviews": 2134,
                "type": 'Private',
                "category": 'Medical',
                "established": 1953,
                "fees": 1800000,
                "placement": 1500000,
                "ranking": 10,
                "featured": False,
                "courses": 65,
                "students": 28000,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "13",
                "name": 'Vellore Institute of Technology',
                "shortName": 'VIT Vellore',
                "location": 'Vellore',
                "state": 'Tamil Nadu',
                "rating": 4.4,
                "reviews": 3567,
                "type": 'Private',
                "category": 'Engineering',
                "established": 1984,
                "fees": 175000,
                "placement": 1200000,
                "ranking": 11,
                "featured": False,
                "courses": 52,
                "students": 35000,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "14",
                "name": 'Indian Statistical Institute',
                "shortName": 'ISI Kolkata',
                "location": 'Kolkata',
                "state": 'West Bengal',
                "rating": 4.7,
                "reviews": 654,
                "type": 'Public',
                "category": 'Science & Research',
                "established": 1931,
                "fees": 100000,
                "placement": 2400000,
                "ranking": 3,
                "featured": True,
                "courses": 12,
                "students": 900,
                "image": '/api/placeholder/400/300'
            },
            {
                "id": "15",
                "name": 'Amity University',
                "shortName": 'Amity Noida',
                "location": 'Noida',
                "state": 'Uttar Pradesh',
                "rating": 4.2,
                "reviews": 4321,
                "type": 'Private',
                "category": 'Arts & Science',
                "established": 2005,
                "fees": 200000,
                "placement": 600000,
                "ranking": 20,
                "featured": False,
                "courses": 95,
                "students": 45000,
                "image": '/api/placeholder/400/300'
            }
        ]

        # Apply filters from query
        filtered_colleges = all_colleges.copy()

        # Name search filter (case-insensitive)
        if 'name' in query and '$regex' in query['name']:
            search_pattern = query['name']['$regex']
            filtered_colleges = [
                c for c in filtered_colleges
                if re.search(search_pattern, c['name'], re.IGNORECASE)
            ]

        # State filter
        if 'state' in query:
            filtered_colleges = [
                c for c in filtered_colleges
                if c['state'] == query['state']
            ]

        # Type filter
        if 'type' in query:
            filtered_colleges = [
                c for c in filtered_colleges
                if c['type'] == query['type']
            ]

        # Category filter
        if 'category' in query:
            filtered_colleges = [
                c for c in filtered_colleges
                if c['category'] == query['category']
            ]

        # Apply sorting
        if sort_criteria:
            sort_field, sort_order = sort_criteria[0]
            reverse = sort_order == -1
            filtered_colleges = sorted(
                filtered_colleges,
                key=lambda x: x.get(sort_field, 0),
                reverse=reverse
            )

        # Calculate pagination
        total = len(filtered_colleges)
        total_pages = (total + page_size - 1) // page_size
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        paginated_colleges = filtered_colleges[start_idx:end_idx]

        # Convert fees and placement back to string format for display
        for college in paginated_colleges:
            print(college['name'])
            college['fees'] = f"₹{college['fees'] / 100000:.1f} Lakhs"
            college['placement'] = f"₹{college['placement'] / 100000:.0f} LPA"

        return CollegeListPageResponse(
            colleges=paginated_colleges,
            total=total,
            page=page,
            size=page_size
        )

    @staticmethod
    async def get_college_data(college_id: int):
        """Get complete college data by ID"""
        college_data = {}
        college_details = CollegeService.get_college_details(college_id)
        college_fee_structure = CollegeService.get_fee_structure(college_id)
        college_placements = CollegeService.get_placements(college_id)
        college_branch_placements = CollegeService.get_branch_placements(college_id)
        college_admissions = CollegeService.get_admissions(college_id)
        college_academics = CollegeService.get_academics(college_id)
        college_departments = CollegeService.get_departments(college_id)
        college_infrastructure = CollegeService.get_infrastructure(college_id)
        college_campus_experience = CollegeService.get_campus_experience(college_id)
        college_clubs = CollegeService.get_clubs(college_id)
        college_events = CollegeService.get_events(college_id)
        college_gallery = CollegeService.get_gallery(college_id)
        college_alumni = CollegeService.get_alumni(college_id)
        college_scholarships = CollegeService.get_scholarships(college_id)
        college_startups = CollegeService.get_startups(college_id)
        college_social_media = CollegeService.get_social_media(college_id)
        college_nearby_places = CollegeService.get_nearby_places(college_id)
        # """Excluded data is college_ratings, college_reviews, news"""

        # Combine all data into a single dictionary
        college_data["college_details"] = college_details
        college_data["college_placements"] = college_placements
        college_data["college_branch_placements"] = college_branch_placements
        college_data["college_departments"] = college_departments
        college_data["college_infrastructure"] = college_infrastructure
        college_data["college_campus_experience"] = college_campus_experience
        college_data["college_clubs"] = college_clubs
        college_data["college_events"] = college_events
        college_data["college_gallery"] = college_gallery
        college_data["college_alumni"] = college_alumni
        college_data["college_scholarships"] = college_scholarships
        college_data["college_startups"] = college_startups
        college_data["college_social_media"] = college_social_media
        college_data["college_nearby_places"] = college_nearby_places
        college_data["college_admissions"] = college_admissions
        college_data["college_academics"] = college_academics
        college_data["college_fee_structure"] = college_fee_structure

        return college_data


    @staticmethod
    def get_college_details(college_id: int) -> dict:
        """Get detailed college information"""
        return {
            "id": college_id,
            "name": "National Institute of Technology Alpha",
            "shortName": "NITA",
            "aboutHTML": "<p>National Institute of Technology Alpha (NITA) is a premier engineering institute located in Dadri, Uttar Pradesh. Established in 1965, NITA has consistently ranked among the top engineering colleges in India, known for its rigorous academics, cutting-edge research, and vibrant campus life.</p>",
            "established": 1965,
            "type": "Public",
            "category": "Engineering",
            "location": {
            "address": "Sector 22, Academic Road",
            "city": "Dadri",
            "state": "Uttar Pradesh",
            "pincode": "203207",
            "coordinates": {"lat": 12.99151, "lng": 80.23362}
            },
            "contact": {
            "phone": ["+91-120-1234567", "+91-120-7654321"],
            "email": ["info@nita.edu.in", "admissions@nita.edu.in"],
            "website": "https://www.nita.edu.in",
            "helpline": {
                    "admission": {
                    "phone": "+91-120-1112223",
                    "email": "admissions@nita.edu.in"
                    },
                    "scholarships": {
                    "phone": "+91-120-3334445",
                    "email": "scholarships@nita.edu.in"
                    },
                    "general": {
                    "phone": "+91-120-4445556",
                    "email": "info@nita.edu.in"
                    }
                }
            }
        }

    @staticmethod
    def get_college_ratings(college_id: int) -> dict:
        """Get college ratings and reviews count"""
        return {
            "overall": 4.3,
            "academics": 4.5,
            "infrastructure": 4.1,
            "faculty": 4.4,
            "placement": 4.2,
            "hostelLife": 3.9,
            "socialLife": 4.0,
            "totalReviews": 1287
        }

    @staticmethod
    def get_college_reviews(college_id: int) -> dict:
        """Get college reviews and testimonials"""
        return {
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
                {"id": "rv1", "name": "Neha Gupta", "program": "B.Tech CSE", "batch": "2024", "content": "Great exposure to coding competitions and projects.", "rating": 5},
                {"id": "rv2", "name": "Rahul Singh", "program": "M.Tech VLSI", "batch": "2023", "content": "Labs are well-equipped; placements are decent.", "rating": 4}
            ]
        }

    @staticmethod
    def get_fee_structure(college_id: int) -> dict:
        """Get college fee structure for all programs"""
        return {
            "undergraduate": [
                {
                    "programe_name": "B.Tech",
                    "description": "General/OBC/EWS with family income above ₹5 Lakhs",
                    "fees": {
                        "admission": 3000,
                        "student_welfare": 1500,
                        "career_pathway_facility": 9500,
                        "alumni_services": 6000,
                        "tuition": 100000,
                        "enrolment": 1500,
                        "medical": 1500,
                        "seat_rent": 7500,
                        "extra_curricular": 2000,
                        "student_wellness": 500,
                        "student_medical_insurance": 2402,
                        "caution_deposit": 5000
                    }
                },
                {
                    "programe_name": "B.Tech",
                    "description": "General/OBC/EWS with family income between ₹1-5 Lakhs",
                    "fees": {
                        "admission": 3000,
                        "student_welfare": 1500,
                        "career_pathway_facility": 9500,
                        "alumni_services": 6000,
                        "tuition": 33333,
                        "enrolment": 1500,
                        "medical": 1500,
                        "seat_rent": 7500,
                        "extra_curricular": 2000,
                        "student_wellness": 500,
                        "student_medical_insurance": 2402,
                        "caution_deposit": 5000
                    }
                },
                {
                    "programe_name": "B.Tech",
                    "description": "General/OBC/EWS with family income below ₹1 Lakh and SC/ST/PwD",
                    "fees": {
                        "admission": 3000,
                        "student_welfare": 1500,
                        "career_pathway_facility": 9500,
                        "alumni_services": 6000,
                        "tuition": 0,
                        "enrolment": 1500,
                        "medical": 1500,
                        "seat_rent": 7500,
                        "extra_curricular": 2000,
                        "student_wellness": 500,
                        "student_medical_insurance": 2402,
                        "caution_deposit": 5000
                    }
                }
            ],
            "postgraduate": [
                {
                    "programe_name": "M.Tech",
                    "description": "General/OBC/EWS",
                    "fees": {
                        "admission": 3000,
                        "student_welfare": 1500,
                        "career_pathway_facility": 9500,
                        "alumni_services": 6000,
                        "tuition": 25000,
                        "enrolment": 1500,
                        "medical": 1500,
                        "seat_rent": 7500,
                        "extra_curricular": 2000,
                        "student_wellness": 500,
                        "student_medical_insurance": 2402,
                        "caution_deposit": 5000
                    }
                },
                {
                    "programe_name": "M.Tech",
                    "description": "SC/ST/PwD",
                    "fees": {
                        "admission": 3000,
                        "student_welfare": 1500,
                        "career_pathway_facility": 9500,
                        "alumni_services": 6000,
                        "tuition": 0,
                        "enrolment": 1500,
                        "medical": 1500,
                        "seat_rent": 7500,
                        "extra_curricular": 2000,
                        "student_wellness": 500,
                        "student_medical_insurance": 2402,
                        "caution_deposit": 5000
                    }
                },
                {
                    "programe_name": "M.Sc",
                    "description": "General/OBC/EWS",
                    "fees": {
                        "admission": 3000,
                        "student_welfare": 1500,
                        "career_pathway_facility": 9500,
                        "alumni_services": 6000,
                        "tuition": 25000,
                        "enrolment": 1500,
                        "medical": 1500,
                        "seat_rent": 7500,
                        "extra_curricular": 2000,
                        "student_wellness": 500,
                        "student_medical_insurance": 2402,
                        "caution_deposit": 5000
                    }
                },
                {
                    "programe_name": "M.Sc",
                    "description": "SC/ST/PwD",
                    "fees": {
                        "admission": 3000,
                        "student_welfare": 1500,
                        "career_pathway_facility": 9500,
                        "alumni_services": 6000,
                        "tuition": 0,
                        "enrolment": 1500,
                        "medical": 1500,
                        "seat_rent": 7500,
                        "extra_curricular": 2000,
                        "student_wellness": 500,
                        "student_medical_insurance": 2402,
                        "caution_deposit": 5000
                    }
                },
                {
                    "programe_name": "M.A",
                    "description": "General/OBC/EWS",
                    "fees": {
                        "admission": 3000,
                        "student_welfare": 1500,
                        "career_pathway_facility": 9500,
                        "alumni_services": 6000,
                        "tuition": 20000,
                        "enrolment": 1500,
                        "medical": 1500,
                        "seat_rent": 7500,
                        "extra_curricular": 2000,
                        "student_wellness": 500,
                        "student_medical_insurance": 2402,
                        "caution_deposit": 5000
                    }
                },
                {
                    "programe_name": "M.A",
                    "description": "SC/ST/PwD",
                    "fees": {
                        "admission": 3000,
                        "student_welfare": 1500,
                        "career_pathway_facility": 9500,
                        "alumni_services": 6000,
                        "tuition": 0,
                        "enrolment": 1500,
                        "medical": 1500,
                        "seat_rent": 7500,
                        "extra_curricular": 2000,
                        "student_wellness": 500,
                        "student_medical_insurance": 2402,
                        "caution_deposit": 5000
                    }
                }
            ],
            "doctoral": [
                {
                    "programe_name": "Ph.D.",
                    "description": "General/OBC/EWS",
                    "fees": {
                        "tuition": 5000,
                        "enrolment": 1500,
                        "medical": 1500,
                        "seat_rent": 7500,
                        "extra_curricular": 2000,
                        "student_wellness": 500,
                        "student_medical_insurance": 2402
                    }
                },
                {
                    "programe_name": "Ph.D.",
                    "description": "SC/ST/PwD",
                    "fees": {
                        "tuition": 0,
                        "enrolment": 1500,
                        "medical": 1500,
                        "seat_rent": 7500,
                        "extra_curricular": 2000,
                        "student_wellness": 500,
                        "student_medical_insurance": 2402
                    }
                }
            ]
        }

    @staticmethod
    def get_placements(college_id: int) -> dict:
        """Get college placement data"""
        return {
            "averagePackage": "INR 10.8 LPA",
            "highestPackage": "INR 52 LPA",
            "placementRate": 86,
            "medianPackage": "INR 9.5 LPA",
            "topRecruiters": ["Google", "Microsoft", "TCS", "Infosys", "Amazon", "Accenture"],
            "internationalOffers": 7,
            "salaryTrends": [
                {"year": 2021, "average": "INR 8.7 LPA", "highest": "INR 32 LPA", "placementRate": 82},
                {"year": 2022, "average": "INR 9.6 LPA", "highest": "INR 40 LPA", "placementRate": 84},
                {"year": 2023, "average": "INR 10.8 LPA", "highest": "INR 52 LPA", "placementRate": 86},
            ],
            "sectorDistribution": [
                {"sector": "IT/Software", "percentage": 52},
                {"sector": "Core Engineering", "percentage": 22},
                {"sector": "Analytics/Consulting", "percentage": 16},
                {"sector": "Product", "percentage": 7},
                {"sector": "Others", "percentage": 3},
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
                    "story": "Riya contributed to open-source projects and led the coding club, which helped her stand out during interviews."
                },
                {
                    "name": "Arjun Patel",
                    "company": "Amazon",
                    "package": "INR 42 LPA",
                    "role": "SDE I",
                    "story": "Focused on system design and interned at a startup, gaining real-world experience before final placements."
                }
            ],
            "placementProcess": [
                { "step": "Pre-Placement Talks", "description": "Companies present their profiles" },
                { "step": "Resume Shortlisting", "description": "Based on CGPA and skills" },
                { "step": "Written Test", "description": "Aptitude and technical assessment" },
                { "step": "Group Discussion", "description": "Communication and teamwork" },
                { "step": "Interviews", "description": "Technical and HR rounds" },
                { "step": "Offer Letter", "description": "Final selection and onboarding" }
            ]
        }

    @staticmethod
    def get_branch_placements(college_id: int) -> dict:
        """Get branch-wise placement data"""
        return {
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
                },
                {
                    "name": "Electronics and Communication Engineering",
                    "averagePackage": "INR 9.8 LPA",
                    "medianPackage": "INR 9.2 LPA",
                    "highestPackage": "INR 28 LPA",
                    "placementRate": 88,
                    "offers": 134,
                    "topRoles": ["Embedded Engineer", "ASIC Design", "Systems Engineer"],
                    "recruiters": ["Qualcomm", "Texas Instruments", "Samsung"]
                },
                {
                    "name": "Mechanical Engineering",
                    "averagePackage": "INR 7.4 LPA",
                    "medianPackage": "INR 7.0 LPA",
                    "highestPackage": "INR 18 LPA",
                    "placementRate": 78,
                    "offers": 96,
                    "topRoles": ["Manufacturing Engineer", "Design Engineer", "Operations"],
                    "recruiters": ["Tata Motors", "Maruti Suzuki", "L&T"]
                }
            ]
        }

    @staticmethod
    def get_admissions(college_id: int) -> dict:
        """Get admission information for all programs and methods, with steps, deadlines, documents, and eligibility"""
        return {
            "overview": "Admissions are offered via multiple methods, each with its own eligibility, documents, and deadlines.",
            "methods": [
                {
                    "type": "Exam-Based",
                    "methods": [
                        {
                            "name": "JEE Main",
                            "applicationPrograms": ["B.Tech"],
                            "eligibility": [
                                "Class 12 with Physics, Chemistry, Mathematics",
                                "Minimum 75% aggregate",
                                "JEE Main score"
                            ],
                            "requiredDocuments": [
                                "Photo ID",
                                "Class 12 Marksheet",
                                "JEE Main Admit Card",
                                "JEE Main Scorecard",
                                "Passport-size photographs",
                                "Caste/Category certificate (if applicable)"
                            ],
                            "steps": [
                                {"step": "Registration", "deadline": "2025-04-30", "link": "https://jeemain.nta.nic.in"},
                                {"step": "Exam Date", "deadline": "2025-05-20"},
                                {"step": "Result Declaration", "deadline": "2025-06-05", "link": "https://jeemain.nta.nic.in"},
                                {"step": "JoSAA Counseling Registration", "deadline": "2025-06-15", "link": "https://josaa.nic.in"},
                                {"step": "Document Verification", "deadline": "2025-07-10"}
                            ]
                        },
                        {
                            "name": "State CET",
                            "applicationPrograms": ["B.Tech"],
                            "eligibility": [
                                "Class 12 with PCM",
                                "State CET score"
                            ],
                            "requiredDocuments": [
                                "Photo ID",
                                "Class 12 Marksheet",
                                "State CET Admit Card",
                                "State CET Scorecard",
                                "Passport-size photographs",
                                "Domicile certificate (if applicable)"
                            ],
                            "steps": [
                                {"step": "Registration", "deadline": "2025-03-31"},
                                {"step": "Exam Date", "deadline": "2025-04-20"},
                                {"step": "Counseling Registration", "deadline": "2025-05-10"},
                                {"step": "Document Verification", "deadline": "2025-06-01"}
                            ]
                        },
                        {
                            "name": "GATE",
                            "applicationPrograms": ["M.Tech"],
                            "eligibility": [
                                "B.E/B.Tech in relevant field",
                                "Valid GATE score"
                            ],
                            "requiredDocuments": [
                                "Photo ID",
                                "B.E/B.Tech Degree Certificate",
                                "GATE Admit Card",
                                "GATE Scorecard",
                                "Passport-size photographs"
                            ],
                            "steps": [
                                {"step": "Registration", "deadline": "2025-05-15"},
                                {"step": "Exam Date", "deadline": "2025-06-10"},
                                {"step": "Interview", "deadline": "2025-07-05"}
                            ]
                        },
                        {
                            "name": "CAT",
                            "applicationPrograms": ["MBA"],
                            "eligibility": [
                                "Any bachelor's degree",
                                "CAT/MAT/XAT score"
                            ],
                            "requiredDocuments": [
                                "Photo ID",
                                "Bachelor's Degree Certificate",
                                "CAT/MAT/XAT Admit Card",
                                "CAT/MAT/XAT Scorecard",
                                "Passport-size photographs"
                            ],
                            "steps": [
                                {"step": "Registration", "deadline": "2025-06-30"},
                                {"step": "Exam Date", "deadline": "2025-07-15"},
                                {"step": "GD & Interview", "deadline": "2025-08-05"}
                            ]
                        }
                    ]
                },
                {
                    "type": "Non-Exam-Based",
                    "methods": [
                        {
                            "name": "Direct Admission / Management Quota",
                            "applicationPrograms": ["B.Tech", "MBA", "M.Tech"],
                            "eligibility": [
                                "Class 12 marks (for UG)",
                                "Bachelor's degree (for PG)",
                                "As per college policy"
                            ],
                            "requiredDocuments": [
                                "Photo ID",
                                "Class 12/Bachelor's Marksheet",
                                "Passport-size photographs",
                                "Caste/Category certificate (if applicable)"
                            ],
                            "steps": [
                                {"step": "Application Submission", "deadline": "2025-07-31"},
                                {"step": "Document Verification", "deadline": "2025-08-10"},
                                {"step": "Fee Payment", "deadline": "2025-08-15"}
                            ]
                        },
                        {
                            "name": "Lateral Entry (LEET)",
                            "applicationPrograms": ["B.Tech (2nd year)"],
                            "eligibility": [
                                "Diploma in Engineering",
                                "LEET score"
                            ],
                            "requiredDocuments": [
                                "Photo ID",
                                "Diploma Marksheet",
                                "LEET Admit Card",
                                "LEET Scorecard",
                                "Passport-size photographs"
                            ],
                            "steps": [
                                {"step": "LEET Registration", "deadline": "2025-05-20"},
                                {"step": "Exam Date", "deadline": "2025-06-10"},
                                {"step": "Counseling", "deadline": "2025-07-01"}
                            ]
                        },
                        {
                            "name": "NRI/International Admissions",
                            "applicationPrograms": ["B.Tech", "MBA", "M.Tech"],
                            "eligibility": [
                                "NRI/Foreign student status",
                                "Class 12/Bachelor's marks"
                            ],
                            "requiredDocuments": [
                                "Photo ID",
                                "Passport",
                                "Class 12/Bachelor's Marksheet",
                                "Proof of NRI/International status",
                                "Passport-size photographs"
                            ],
                            "steps": [
                                {"step": "Application Submission", "deadline": "2025-06-30"},
                                {"step": "Document Verification", "deadline": "2025-07-15"},
                                {"step": "Fee Payment", "deadline": "2025-07-31"}
                            ]
                        },
                        {
                            "name": "Special Category Admissions",
                            "applicationPrograms": ["All"],
                            "eligibility": [
                                "Eligibility as per quota (Sports/Defense/Minority/EWS/SC/ST/OBC)"
                            ],
                            "requiredDocuments": [
                                "Photo ID",
                                "Quota certificate",
                                "Class 12/Bachelor's Marksheet",
                                "Passport-size photographs"
                            ],
                            "steps": [
                                {"step": "Quota Application", "deadline": "2025-06-30"},
                                {"step": "Document Submission", "deadline": "2025-07-10"},
                                {"step": "Verification", "deadline": "2025-07-20"}
                            ]
                        }
                    ]
                }
            ],
            "generalGuidelines": [
                "Ensure all documents are uploaded in the correct format in the admission portal.",
                "Track your application status on the admissions portal.",
                "Contact the admissions helpline for any queries."
            ],
            "importantLinks": [
                {"label": "Official Admissions Portal", "url": "https://www.nita.edu.in/admissions"},
                {"label": "JEE Main Website", "url": "https://jeemain.nta.nic.in"},
                {"label": "GATE Official Site", "url": "https://gate.iitb.ac.in"},
                {"label": "CAT Official Site", "url": "https://iimcat.ac.in"}
            ],
            "faqs": [
                {"question": "What is the application fee for B.Tech admissions?",
                    "answer": "The application fee for B.Tech admissions via JEE Main is INR 650 for General category and INR 325 for SC/ST/PwD categories."
                },
                {
                    "question": "Can I apply for multiple programs?",
                    "answer": "Yes, you can apply for multiple programs, but ensure you meet the eligibility criteria for each."
                },
                {
                    "question": "What are the scholarship options available?",
                    "answer": "Various scholarships are available based on merit, category, and financial need. Check the scholarships section on the official website for details."
                }
            ]
        }

    @staticmethod
    def get_academics(college_id: int) -> dict:
        """Get academic information"""
        return {
            "courses": [
                {
                    "name": "Computer Science and Engineering",
                    "duration": "4 years",
                    "graduation_level": "Undergraduate",
                    "degree": "B.Tech",
                    "fees": "INR 1,20,000 per year",
                    "classroom_size": "30 students",
                    "hod": {
                        "name": "Dr. Alice Smith",
                        "image": "https://picsum.photos/seed/alicesmith/400/400",
                        "mobile": "+91-9876543210",
                        "email": "alice.smith@university.edu"
                    }
                },
                {
                    "name": "Electronics and Communication Engineering",
                    "duration": "4 years",
                    "graduation_level": "Undergraduate",
                    "degree": "B.Tech",
                    "fees": "INR 1,18,000 per year",
                    "classroom_size": "30 students",
                    "hod": {
                        "name": "Dr. Bob Johnson",
                        "image": "https://picsum.photos/seed/bobjohnson/400/400",
                        "mobile": "+91-8765432109",
                        "email": "bob.johnson@university.edu"
                    }
                },
                {
                    "name": "Physics",
                    "duration": "3 years",
                    "graduation_level": "Undergraduate",
                    "degree": "B.Sc",
                    "fees": "INR 60,000 per year",
                    "hod": {
                        "name": "Dr. Bob Johnson",
                        "image": "https://picsum.photos/seed/bobjohnson/400/400",
                        "mobile": "+91-8765432109",
                        "email": "bob.johnson@university.edu"
                    }
                },
                {
                    "name": "Computer Science and Engineering",
                    "duration": "2 years",
                    "graduation_level": "Postgraduate",
                    "degree": "M.Tech",
                    "fees": "INR 1,50,000 per year",
                    "hod": {
                        "name": "Dr. Bob Johnson",
                        "image": "https://picsum.photos/seed/bobjohnson/400/400",
                        "mobile": "+91-8765432109",
                        "email": "bob.johnson@university.edu"
                    }
                },
                {
                    "name": "VLSI Design",
                    "duration": "2 years",
                    "graduation_level": "Postgraduate",
                    "degree": "M.Tech",
                    "fees": "INR 1,48,000 per year",
                    "hod": {
                        "name": "Dr. Bob Johnson",
                        "image": "https://picsum.photos/seed/bobjohnson/400/400",
                        "mobile": "+91-8765432109",
                        "email": "bob.johnson@university.edu"
                    }
                },
                {
                    "name": "Computer Science",
                    "duration": "3-5 years",
                    "graduation_level": "Doctorate",
                    "degree": "PhD",
                    "fees": "INR 50,000 per year"
                }
            ],
            "certifications": [
                {
                    "name": "Data Science Professional Certificate",
                    "duration": "6 months",
                    "eligibility": "Any undergraduate student",
                    "fees": "INR 16,000"
                },
                {
                    "name": "Cybersecurity Fundamentals",
                    "duration": "4 months",
                    "eligibility": "Engineering students",
                    "fees": "INR 12,000"
                },
                {
                    "name": "Business Analytics",
                    "duration": "3 months",
                    "eligibility": "MBA students",
                    "fees": "INR 10,000"
                }
            ]
        }

    @staticmethod
    def get_departments(college_id: int) -> dict:
        """Get department information with faculty details"""
        return {
            "departments": [
                {
                    "id": "cse",
                    "name": "Computer Science and Engineering",
                    "summary": "Focus on algorithms, systems, AI/ML, and software engineering.",
                    "strengths": ["Competitive programming culture", "Strong research output", "Industry collaboration"],
                    "undergraduateCourses": ["Data Structures", "Operating Systems", "DBMS", "AI Fundamentals"],
                    "postgraduateCourses": ["Advanced Algorithms", "Distributed Systems", "Deep Learning"],
                    "phdCourses": ["Research Methodology in CS", "Advanced Topics in ML"],
                    "faculty": [
                        {
                            "name": "Dr. Alice Smith",
                            "designation": "Professor",
                            "researchInterests": ["Machine Learning", "Data Mining"]
                        },
                        {
                            "name": "Dr. Bob Johnson",
                            "designation": "Associate Professor",
                            "researchInterests": ["Computer Vision", "Robotics"]
                        }
                    ]
                },
                {
                    "id": "ece",
                    "name": "Electronics and Communication Engineering",
                    "summary": "VLSI, embedded systems, signal processing, and communications.",
                    "strengths": ["Modern labs", "Chip design projects", "Industry MoUs"],
                    "undergraduateCourses": ["Signals and Systems", "Digital Electronics", "Communication Systems"],
                    "postgraduateCourses": ["VLSI Design", "Embedded Systems", "Wireless Networks"],
                    "phdCourses": ["Advanced Signal Processing", "SoC Design"],
                    "faculty": [
                        {
                            "name": "Dr. Carol Lee",
                            "image": "https://picsum.photos/seed/carollee/400/400",
                            "designation": "Professor",
                            "researchInterests": ["VLSI Design", "Nanoelectronics"]
                        },
                        {
                            "name": "Dr. David Kim",
                            "image": "https://picsum.photos/seed/davidkim/400/400",
                            "designation": "Assistant Professor",
                            "researchInterests": ["Wireless Communications", "IoT"]
                        }
                    ]
                }
            ]
        }

    @staticmethod
    def get_infrastructure(college_id: int) -> dict:
        """Get infrastructure details"""
        return {
            "overview": "A 300-acre green campus with modern labs, libraries, and student-centric spaces.",
            "keyHighlights": [
                "Central library with 1.2 lakh volumes",
                "High-speed campus Wi-Fi",
                "Incubation center and maker labs"
            ],
            "campus": {"area": "300 acres", "buildings": 28, "labs": 64, "libraries": 3},
            "facilities": [
                "Auditorium", "Seminar Halls", "Innovation Lab", "Cafeterias", "Health Center", "ATM", "Post Office"
            ],
            "hostels": [
                {
                    "name": "Aryabhatta Hostel",
                    "capacity": 1200,
                    "rooms": "Double occupancy, AC/Non-AC options",
                    "facilities": ["Laundry", "Common rooms", "Mess", "Reading rooms", "24x7 security", "Library"],
                    "gallery": ["https://picsum.photos/seed/hostel1/800/400", "https://picsum.photos/seed/hostel2/800/400"],
                    "description": "One of the largest hostels with modern amenities and a vibrant student community.",
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
                    "focus": "Applied AI, robotics, autonomous systems",
                    "description": "Supports student and faculty projects, hackathons, and industry partnerships.",
                    "link": "https://www.nita.edu.in/ai-center",
                    "gallery": [
                        "https://picsum.photos/seed/ai1/800/400",
                        "https://picsum.photos/seed/ai2/800/400"
                    ]
                },
                {
                    "name": "Sustainable Energy Lab",
                    "focus": "Solar microgrids, storage, smart energy",
                    "description": "Pilot projects with local utilities, student-led research.",
                    "link": "",
                    "gallery": [
                        "https://picsum.photos/seed/energy1/800/400",
                        "https://picsum.photos/seed/energy2/800/400"
                    ]
                }
            ],
            "digitalInfrastructure": [
                "25 Gbps backbone",
                "Smart classrooms",
                "Cloud-based LMS",
                "Virtual lab access",
                "Super computing cluster"
            ],
            "sustainabilityInitiatives": [
                {"title": "Solar PV across hostels", "impact": "Cuts 20% grid usage"},
                {"title": "Rainwater harvesting", "impact": "Reduces freshwater demand by 30%"}
            ],
            "transport": [
                {"mode": "Campus shuttle", "frequency": "Every 15 minutes"},
                {"mode": "City bus connectivity", "frequency": "Hourly"}
            ]
        }

    @staticmethod
    def get_campus_experience(college_id: int) -> dict:
        """Get campus life experience information"""
        return {
            "lifestyleHighlights": [
            {"title": "Festive campus", "description": "Annual tech, cultural, and sports fests bring the campus alive."},
            {"title": "Peer learning", "description": "Clubs and labs foster collaborative projects and knowledge sharing."}
            ],
            "supportServices": [
            {"name": "Counseling Center", "description": "Mental health support and mentoring."},
            {"name": "Career Services", "description": "Internships, placements, resume workshops."}
            ],
            "diningOptions": [
            {
                "name": "Central Mess",
                "type": "Veg/Non-veg",
                "signature": "Thali, biryani",
                "openTill": "22:00",
                "gallery": [
                {
                    "url": "https://picsum.photos/seed/centralmess1/800/400",
                    "description": "Main dining hall of Central Mess",
                    "year": 2023,
                    "photographerCredit": "Ravi Kumar"
                },
                {
                    "url": "https://picsum.photos/seed/centralmess2/800/400",
                    "description": "Food counter at Central Mess",
                    "year": 2023,
                    "photographerCredit": "Priya Sharma"
                }
                ]
            },
            {
                "name": "Cafe Byte",
                "type": "Cafe",
                "signature": "Sandwiches, coffee",
                "openTill": "23:00",
                "gallery": [
                {
                    "url": "https://picsum.photos/seed/cafebyte1/800/400",
                    "description": "Interior view of Cafe Byte",
                    "year": 2024,
                    "photographerCredit": "Amit Verma"
                },
                {
                    "url": "https://picsum.photos/seed/cafebyte2/800/400",
                    "description": "Coffee bar at Cafe Byte",
                    "year": 2024,
                    "photographerCredit": "Neha Gupta"
                }
                ]
            }
            ],
            "sportsAndFitness": [
            {
                "name": "Indoor stadium",
                "details": "Badminton, table tennis",
                "openTill": "21:00",
                "gallery": [
                {
                    "url": "https://picsum.photos/seed/indoorstadium1/800/400",
                    "description": "Badminton courts in indoor stadium",
                    "year": 2023,
                    "photographerCredit": "Suresh Patel"
                },
                {
                    "url": "https://picsum.photos/seed/indoorstadium2/800/400",
                    "description": "Table tennis area",
                    "year": 2023,
                    "photographerCredit": "Vikram Singh"
                }
                ]
            },
            {
                "name": "Fitness center",
                "details": "Weights, cardio",
                "gallery": [
                {
                    "url": "https://picsum.photos/seed/fitnesscenter1/800/400",
                    "description": "Cardio equipment section",
                    "year": 2024,
                    "photographerCredit": "Anjali Reddy"
                },
                {
                    "url": "https://picsum.photos/seed/fitnesscenter2/800/400",
                    "description": "Weight training area",
                    "year": 2024,
                    "photographerCredit": "Karan Mehta"
                }
                ]
            }
            ],
            "wellnessPrograms": [
            {"name": "Mindful Mondays", "description": "Guided meditation and stress relief."},
            {"name": "Health Camps", "description": "Quarterly check-ups and nutrition advice."}
            ],
            "residential": [
              {
            "name": "Sunrise Hostel",
            "hostel_type": "boys",
            "capacity": 200,
            "rooms": "Single, Double",
            "facilities": ["Wi-Fi", "Laundry", "Common Room", "Mess"],
            "gallery": [
              {
                "url": "https://picsum.photos/seed/sunrise1/800/400",
                "description": "Front view of Sunrise Hostel",
                "year": 2023,
                "photographerCredit": "John Doe",
              },
              {
                "url": "https://picsum.photos/seed/sunrise2/800/400",
                "description": "Common room in Sunrise Hostel",
                "year": 2023,
                "photographerCredit": "Jane Smith",
              },
            ],
            "description": "A modern boys' hostel with all essential amenities.",
            "reviews": [
              {
                "student": "Rahul Sharma",
                "batch": "2024",
                "comment": "The hostel is clean and well-maintained. Food quality is good.",
                "ratings": {
                  "cleanliness": 4,
                  "management": 4,
                  "infrastructure": 5,
                  "overall": 4,
                },
              },
              {
                "student": "Amit Verma",
                "batch": "2023",
                "comment": "Great facilities but the Wi-Fi speed could be improved.",
                "ratings": {
                  "cleanliness": 5,
                  "management": 3,
                  "infrastructure": 4,
                  "overall": 4,
                },
              },
            ],
              },
              {
            "name": "Moonlight Hostel",
            "hostel_type": "girls",
            "capacity": 150,
            "rooms": "Single, Triple",
            "facilities": ["Wi-Fi", "24/7 Security", "Gym", "Mess"],
            "gallery": [
              {
                "url": "https://picsum.photos/seed/moonlight1/800/400",
                "description": "Entrance of Moonlight Hostel",
                "year": 2023,
                "photographerCredit": "Alice Johnson",
              },
              {
                "url": "https://picsum.photos/seed/moonlight2/800/400",
                "description": "Dining area in Moonlight Hostel",
                "year": 2023,
                "photographerCredit": "Bob Brown",
              },
            ],
            "description": "A safe and secure hostel for girls with modern facilities.",
            "reviews": [
              {
                "student": "Priya Singh",
                "batch": "2025",
                "comment": "The hostel is very secure and the gym is well-equipped.",
                "ratings": {
                  "cleanliness": 5,
                  "management": 4,
                  "infrastructure": 5,
                  "overall": 5,
                },
              },
              {
                "student": "Anjali Mehta",
                "batch": "2024",
                "comment": "The rooms are spacious and the staff is very helpful.",
                "ratings": {
                  "cleanliness": 4,
                  "management": 5,
                  "infrastructure": 4,
                  "overall": 4,
                },
              },
            ],
              },
              {
            "name": "Starlight Hostel",
            "hostel_type": "co-ed",
            "capacity": 150,
            "rooms": "Single, Triple",
            "facilities": ["Wi-Fi", "24/7 Security", "Gym", "Mess"],
            "gallery": [
              {
                "url": "https://picsum.photos/seed/starlight1/800/400",
                "description": "Entrance of Starlight Hostel",
                "year": 2023,
                "photographerCredit": "Alice Johnson",
              },
              {
                "url": "https://picsum.photos/seed/starlight2/800/400",
                "description": "Dining area in Starlight Hostel",
                "year": 2023,
                "photographerCredit": "Bob Brown",
              },
            ],
            "description": "A safe and secure co-ed hostel with modern facilities.",
            "reviews": [
              {
                "student": "Priya Singh",
                "batch": "2025",
                "comment": "The hostel is very secure and the gym is well-equipped.",
                "ratings": {
                  "cleanliness": 5,
                  "management": 4,
                  "infrastructure": 5,
                  "overall": 5,
                },
              },
              {
                "student": "Anjali Mehta",
                "batch": "2024",
                "comment": "The rooms are spacious and the staff is very helpful.",
                "ratings": {
                  "cleanliness": 4,
                  "management": 5,
                  "infrastructure": 4,
                  "overall": 4,
                },
              },
            ],
              },
            ]
          }

    @staticmethod
    def get_clubs(college_id: int) -> dict:
        """Get college clubs information"""
        return {
            "clubs": [
                {
                    "id": "coding",
                    "name": "Coding Club",
                    "description": "Competitive programming, hackathons, open-source contributions.",
                    "achievements": ["ICPC Regionals top 10", "Google Summer of Code selections"],
                    "contactEmail": "coding.club@nita.edu.in",
                    "social": {
                        "instagram": "https://instagram.com/nita_coding",
                        "youtube": "https://youtube.com/@nita_coding",
                        "linkedin": "https://linkedin.com/company/nita-coding"
                    },
                    # "mediaEmbed": "<iframe src='https://www.youtube.com/embed/dQw4w9WgXcQ' />"
                },
                {
                    "id": "robotics",
                    "name": "Robotics Society",
                    "description": "Design, build, and compete in robotics challenges.",
                    "achievements": ["National Robocon finalist", "Autonomous rover award"],
                    "contactEmail": "robotics@nita.edu.in",
                    "social": { "instagram": "https://instagram.com/nita_robotics" }
                }
            ]
        }

    @staticmethod
    def get_events(college_id: int) -> dict:
        """Get college events information"""
        return {
            "events": [
                {
                    "id": "techfest25",
                    "name": "TechFest 2025",
                    "type": "Technical",
                    "description": "Workshops, coding contests, robotics showdowns.",
                    "date": "2025-11-15",
                    "image": "https://picsum.photos/seed/techfest/800/400",
                    "location": "Main Auditorium",
                    "registrationLink": "https://www.nita.edu.in/techfest",
                    "highlights": ["Keynote by industry leader", "24h hackathon", "Robotics expo"],
                    "social": { "instagram": "https://instagram.com/nita_techfest", "website": "https://www.nita.edu.in/techfest" },
                    # "mediaEmbed": "<iframe src='https://player.vimeo.com/video/123456' />"
                },
                {
                    "id": "cultural25",
                    "name": "Cultura 2025",
                    "type": "Cultural",
                    "description": "Music, dance, drama, and food carnival.",
                    "date": "2025-12-05",
                    "image": "https://picsum.photos/seed/cultura/800/400",
                    "location": "Open Air Theatre",
                    "registrationLink": "https://www.nita.edu.in/cultura",
                    "highlights": ["Battle of bands", "Street play", "Food stalls"],
                    "social": { "instagram": "https://instagram.com/nita_cultura" }
                }
            ]
        }

    @staticmethod
    def get_gallery(college_id: int) -> dict:
        """Get college gallery images"""
        return {
            "images": {
                "campus": [
                    {
                        "description": "Aerial view of NITA campus",
                        "url": "https://picsum.photos/seed/campus1/1200/800",
                        "date": "2024-10-10"
                    },
                    {
                        "description": "Main academic building",
                        "url": "https://picsum.photos/seed/campus2/1200/800",
                        "date": "2024-10-11"
                    }
                ],
                "hostel": [
                    {
                        "description": "Aryabhatta Hostel exterior",
                        "url": "https://picsum.photos/seed/hostel1/1200/800",
                        "date": "2024-10-11"
                    },
                    {
                        "description": "Brahmaputra Hostel interior",
                        "url": "https://picsum.photos/seed/hostel2/1200/800",
                        "date": "2024-10-11"
                    }
                ],
                "facilities": [
                    {
                        "description": "Central Library reading hall",
                        "url": "https://picsum.photos/seed/library/1200/800",
                        "date": "2024-10-11"
                    },
                    {
                        "description": "Computer Lab",
                        "url": "https://picsum.photos/seed/lab/1200/800",
                        "date": "2024-10-11"
                    }
                ],
                "events": [
                    {
                        "description": "TechFest 2024 hackathon",
                        "url": "https://picsum.photos/seed/event1/1200/800",
                        "date": "2024-10-12"
                    },
                    {
                        "description": "Cultura 2024 dance performance",
                        "url": "https://picsum.photos/seed/event2/1200/800",
                        "date": "2024-10-13"
                    }
                ]
            }
        }

    @staticmethod
    def get_alumni(college_id: int) -> dict:
        """Get alumni network information"""
        return {
            "totalAlumni": 18500,
            "notableAlumni": [{'name': 'Abhishek Srivastava',
'position': 'Founder and CEO',
'organisation': 'Techcanvass',
'image': 'https://cache.careers360.mobi/media/colleges/alumni/Abhishek_Srivastava.jpeg?w=48&h=48',
'batch': None,
'branch': None,
'achievement': None},
{'name': 'Binod Singh',
'position': 'Founder President, CEO - Chicago and Bangalore',
'organisation': 'Ilantus Technologies',
'image': 'https://cache.careers360.mobi/media/colleges/alumni/Binod_Singh.jpeg?w=48&h=48',
'batch': None,
'branch': None,
'achievement': None},
{'name': 'Kunal Singh',
'position': 'Head, Business Development - Gears Division - India',
'organisation': 'Mahindra & Mahindra Limited',
'image': 'https://cache.careers360.mobi/media/colleges/alumni/Kunal_Singh.jpeg?w=48&h=48',
'batch': None,
'branch': None,
'achievement': None},
{'name': 'Nitish Kumar',
'position': 'Politician; Current Chief Minister of Bihar',
'organisation': None,
'image': 'https://cache.careers360.mobi/media/colleges/alumni/Nitish_Kumar.webp?w=48&h=48',
'batch': 1973,
'branch': None,
'achievement': None},
{'name': 'Saket Kumar Jha',
'position': 'Group VP - Enterprise Sales',
'organisation': 'Netcore Solutions',
'image': 'https://cache.careers360.mobi/media/colleges/alumni/Saket_Kumar_Jha.jpeg?w=48&h=48',
'batch': None,
'branch': None,
'achievement': None},
{'name': 'Vivek Sharma',
'position': 'Partner',
'organisation': None,
'image': 'https://cache.careers360.mobi/media/colleges/alumni/Vivek_Sharma.jpeg?w=48&h=48',
'batch': None,
'branch': None,
'achievement': None},
{'name': 'Bindeshwari Dubey',
'position': None,
'organisation': None,
'image': None,
'batch': None,
'branch': None,
'achievement': 'Former Chief Minister of Bihar'},
{'name': 'Ratan Kumar Sinha',
'position': 'Chairman, Atomic Energy Commission of India (AEC); Secretary, Department of Atomic Energy (DAE)',
'organisation': None,
'image': None,
'batch': None,
'branch': None,
'achievement': None},
{'name': 'P. A. (Purno Agitok) Sangma',
'position': None,
'organisation': None,
'image': None,
'batch': None,
'branch': None,
'achievement': 'Former Chief Minister of Meghalaya'},
{'name': 'Bhubaneswar Behera',
'position': None,
'organisation': None,
'image': None,
'batch': None,
'branch': None,
'achievement': 'Engineer, writer and scholar'},
{'name': 'Manas Bihari Verma',
'position': None,
'organisation': None,
'image': None,
'batch': None,
'branch': None,
'achievement': 'Indian aeronautical scientist'},
{'name': 'N. K. Sarasdar',
'position': 'Retired professor of the institute',
'organisation': None,
'image': None,
'batch': 1958,
'branch': None,
'achievement': None},
{'name': 'Arun Kumar',
'position': None,
'organisation': None,
'image': None,
'batch': 1969,
'branch': None,
'achievement': None},
{'name': 'Deepak Prakash',
'position': None,
'organisation': None,
'image': None,
'batch': 1994,
'branch': None,
'achievement': None},
{'name': 'Chakradhar Narayan',
'position': None,
'organisation': None,
'image': None,
'batch': 1959,
'branch': None,
'achievement': 'Felicitated — diamond jubilee'},
{'name': 'Sheo Pujan',
'position': None,
'organisation': None,
'image': None,
'batch': 1959,
'branch': None,
'achievement': 'Felicitated — diamond jubilee'},
{'name': 'Umeshwar Prasad',
'position': None,
'organisation': None,
'image': None,
'batch': 1959,
'branch': None,
'achievement': 'Felicitated — diamond jubilee'},
{'name': 'Krishna Deo',
'position': None,
'organisation': None,
'image': None,
'batch': 1959,
'branch': None,
'achievement': 'Felicitated — diamond jubilee'},
{'name': 'Awadh Kishory',
'position': None,
'organisation': None,
'image': None,
'batch': 1959,
'branch': None,
'achievement': 'Felicitated — diamond jubilee'},
{'name': 'Gopal Rao',
'position': None,
'organisation': None,
'image': None,
'batch': 1959,
'branch': None,
'achievement': 'Felicitated — diamond jubilee'},
{'name': 'Rameshwar Prasad',
'position': None,
'organisation': None,
'image': None,
'batch': 1959,
'branch': None,
'achievement': 'Felicitated — diamond jubilee'},
{'name': 'Rajendra Gupta',
'position': None,
'organisation': None,
'image': None,
'batch': 1959,
'branch': None,
'achievement': 'Felicitated — diamond jubilee'},
{'name': 'Akansha Sachdeva',
'position': None,
'organisation': None,
'image': None,
'batch': 2018,
'branch': 'BTech, Civil Engineering',
'achievement': 'Topper'},
{'name': 'Shivans Singh',
'position': None,
'organisation': None,
'image': None,
'batch': 2018,
'branch': 'BTech, Computer Science & Engineering',
'achievement': 'Topper'},
{'name': 'Kumar Piyush',
'position': None,
'organisation': None,
'image': None,
'batch': 2018,
'branch': 'BTech, Electronics & Communications Engineering',
'achievement': 'Topper'},
{'name': 'Vishal Verma',
'position': None,
'organisation': None,
'image': None,
'batch': 2018,
'branch': 'BTech, Electrical Engineering',
'achievement': 'Topper'},
{'name': 'Chitranjan Kumar Jha',
'position': None,
'organisation': None,
'image': None,
'batch': 2018,
'branch': 'BTech, Mechanical Engineering',
'achievement': 'Topper'},
{'name': 'Piyush Kumar Singh',
'position': None,
'organisation': None,
'image': None,
'batch': 2018,
'branch': 'MTech, Civil Engineering',
'achievement': 'Topper'},
{'name': 'Nikhil Nigam',
'position': None,
'organisation': None,
'image': None,
'batch': 2016,
'branch': 'B.Tech., Electrical Engineering',
'achievement': 'Completed Higher Education'}]
        }

    @staticmethod
    def get_scholarships(college_id: int) -> dict:
        """Get scholarships information"""
        return {
            'scholarships': [{'name': 'Notification for the National Scholarship - Academic Year 2025-2026',
  'benefits': [],
  'eligibility': [],
  'description': 'Provides scholarship support for students for the 2025-2026 academic year.',
  'deadline': None,
  'referenceLink': 'https://www.nitp.ac.in/Student/Scholarship'},
 {'name': 'Notification for National Fellowship and Scholarship for Higher Education of ST Students for the Academic Year 2025-2026',
  'benefits': [],
  'eligibility': [],
  'description': "Provides fellowship and scholarships for ST students' higher education in 2025-2026.",
  'deadline': None,
  'referenceLink': 'https://www.nitp.ac.in/Student/Scholarship'},
 {'name': 'NIT Patna Scholarships (merit-cum-means basis)',
  'benefits': [],
  'eligibility': ['Needy students on merit-cum-means basis'],
  'description': 'Provide financial aid to needy students based on merit and means.',
  'deadline': None,
  'referenceLink': 'https://www.collegedekho.com/colleges/nit-patna-scholarship'},
 {'name': 'Minority scholarship for meritorious minority students sponsored by the Minority Commission of Ranchi, Jharkhand',
  'benefits': ['Rs. 17,000'],
  'eligibility': ['Meritorious minority students'],
  'description': 'Financial award for meritorious minority students.',
  'deadline': None,
  'referenceLink': 'https://www.collegedekho.com/colleges/nit-patna-scholarship'},
 {'name': 'Odisha SC/ST Development Board Scholarship (for NIT Patna)',
  'benefits': ['Rs. 49,780'],
  'eligibility': ['Meritorious SC and ST students'],
  'description': 'Financial support for meritorious SC and ST students.',
  'deadline': None,
  'referenceLink': 'https://www.collegedekho.com/colleges/nit-patna-scholarship'},
 {'name': 'IOCL Scholarship for Scheduled Caste candidates',
  'benefits': ['More than Rs. 1,00,000'],
  'eligibility': ['Scheduled Caste candidates'],
  'description': 'Financial scholarship for Scheduled Caste candidates.',
  'deadline': None,
  'referenceLink': 'https://www.collegedekho.com/colleges/nit-patna-scholarship'},
 {'name': 'Various state and central government scholarships (25+ schemes mentioned)',
  'benefits': [],
  'eligibility': [],
  'description': 'Government-sponsored scholarships offering student financial assistance.',
  'deadline': None,
  'referenceLink': 'https://www.collegedekho.com/colleges/nit-patna-scholarship'}]
        }

    @staticmethod
    def get_news(college_id: int, search: Optional[str] = None, page: int = 1, limit: int = 10) -> dict:
        """Get college news with filtering and pagination"""
        all_news = [
            {"id": "n1", "title": "NITA hosts National Robotics Championship", "date": "2025-10-15", "category": "Events", "excerpt": "Students from 50+ colleges compete", "image": "https://picsum.photos/seed/news1/800/400"},
            {"id": "n2", "title": "Research paper published in Nature", "date": "2025-10-10", "category": "Research", "excerpt": "Faculty breakthrough in quantum computing", "image": "https://picsum.photos/seed/news2/800/400"},
            {"id": "n3", "title": "New AI lab inaugurated", "date": "2025-10-05", "category": "Infrastructure", "excerpt": "State-of-the-art facility for ML research", "image": "https://picsum.photos/seed/news3/800/400"},
            {"id": "n4", "title": "Student startup raises $2M funding", "date": "2025-09-28", "category": "Startups", "excerpt": "Edtech platform sees rapid growth", "image": "https://picsum.photos/seed/news4/800/400"},
            {"id": "n5", "title": "Campus recruitment drives exceed targets", "date": "2025-09-20", "category": "Placements", "excerpt": "Record offers from top companies", "image": "https://picsum.photos/seed/news5/800/400"}
        ]
        
        filtered_news = all_news
        if search:
            filtered_news = [n for n in all_news if search.lower() in n['title'].lower() or search.lower() in n['excerpt'].lower()]
        
        total = len(filtered_news)
        start_idx = (page - 1) * limit
        end_idx = start_idx + limit
        paginated_news = filtered_news[start_idx:end_idx]
        
        return {
            "items": paginated_news,
            "total": total,
            "page": page,
            "limit": limit
        }

    @staticmethod
    def get_startups(college_id: int) -> dict:
        """Get college startups information"""
        return {
        "startups": [
            {
            "startup_name": "Ather Energy",
            "description": "Electric scooter manufacturer headquartered in Bengaluru, India.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/67c820b712d3f9eac839c0d6_67c0169dff8d1640b179ea59_ather-logo-1.png",
            "tags": [
                "Manufacturing"
            ]
            },
            {
            "startup_name": "Darwinbox",
            "description": "HR software company offering AI-powered SaaS solutions.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774ea33e0905a2ce6629e_66ece191ff13a3911958ce5b_thedarwinbox_logo%2520(1).jpeg",
            "tags": [
                "AI",
                "Software",
                "SaaS"
            ]
            },
            {
            "startup_name": "EaseMyTrip",
            "description": "Online travel booking platform based in New Delhi.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774ecfc5985eb0379d5fe_66d80383c4a7a00f4fc20772_easemytrip_com_logo%2520sq.jpeg",
            "tags": [
                "Travel"
            ]
            },
            {
            "startup_name": "HighRadius",
            "description": "Cloud-based treasury and finance automation software provider.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774f296e04ee61ed1b8c3_66e9ab56f1db83ebb12ee901_highradius_logo.jpeg",
            "tags": [
                "Software"
            ]
            },
            {
            "startup_name": "OfBusiness",
            "description": "B2B e-commerce platform for business loans and procurement.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774fccff5d687145afe91_66e3b60384a62b477943652e_1631308480506.jpeg",
            "tags": [
                "B2B",
                "Finance"
            ]
            },
            {
            "startup_name": "Perplexity AI",
            "description": "AI-powered search and answer engine for users.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774fee6eeb2b64ce49831_66d7f44dbfa3994bd1ee4091_perplexity_ai_logo.jpeg",
            "tags": [
                "AI"
            ]
            },
            {
            "startup_name": "Rubrik",
            "description": "Cloud data management and backup security platform.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/67777503e4ccf0c35c97c4b6_66e2c44bd67fe858c761fa27_rubrik_inc_logo.jpeg",
            "tags": [
                "Software"
            ]
            },
            {
            "startup_name": "SUGAR Cosmetics",
            "description": "Direct-to-consumer beauty and cosmetics brand in India.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/67c820e05a398dc81eaf5cdd_67c01735a9dc6902362c35e7_sugar_cosmetics_logo.jpeg",
            "tags": [
                "FMCG"
            ]
            },
            {
            "startup_name": "Swiggy",
            "description": "Online food delivery and logistics platform in India.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/6777750767bc7ca53dd53999_66d805c22a3c691e2b8d468f_swiggy_in_logo.jpeg",
            "tags": [
                "Logistics"
            ]
            },
            {
            "startup_name": "Urban Ladder",
            "description": "Online furniture and home d\u00e9cor e-commerce platform.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/6777750d4a45a843d577fda9_66e3b8871e42960a2e9c0426_urban_ladder_logo.jpeg",
            "tags": [
                "Interiors"
            ]
            },
            {
            "startup_name": "Zetwerk",
            "description": "B2B manufacturing marketplace connecting buyers with factories.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/67777513fb1b840b2c09f1bf_66e3b7a6b955c165784c5dd3_zetwerk_in_logo.jpeg",
            "tags": [
                "Manufacturing"
            ]
            },
            {
            "startup_name": "Zoho",
            "description": "Cloud-based suite of business productivity and CRM.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/67777513fb1b840b2c09f204_66e2c53c1324195ec6f3928d_zoho_logo.jpeg",
            "tags": [
                "Software",
                "SaaS"
            ]
            },
            {
            "startup_name": "AmbitionBox",
            "description": "Company reviews and salary insights platform for professionals.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774de62f5fe498fabd331_66d7faa246daee056e722619_ambition_box_logo.jpeg",
            "tags": [
                "Internet"
            ]
            },
            {
            "startup_name": "CleverTap",
            "description": "Customer engagement and analytics platform for mobile businesses.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774e5a2c527caaad530ad_66d7faaf040da82e419d060c_clevertap_logo.jpeg",
            "tags": [
                "Software",
                "SaaS"
            ]
            },
            {
            "startup_name": "Clueso",
            "description": "Conversational AI platform delivering contextual user experiences.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774e6d5d29a63f891cf6b_66d7fabc1a2bf9c9c81f63fc_clueso_logo.jpeg",
            "tags": [
                "Software",
                "SaaS"
            ]
            },
            {
            "startup_name": "CoreVoice",
            "description": "Consulting services focused on voice technology solutions.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774e9ac0b508c34b587b6_66d7fb5553161a5e930bf23d_corevoice_logo.jpeg",
            "tags": [
                "Consulting"
            ]
            },
            {
            "startup_name": "HyperVerge",
            "description": "AI-based image and video recognition technology provider.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774f3d2deebfe71893009_66d7fb0e442363e0981edddd_hyperverge_inc__logo.jpeg",
            "tags": [
                "Software"
            ]
            },
            {
            "startup_name": "Internshala",
            "description": "Online internship and training platform for students.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774f5a1bdece29af53ea0_66d6f3a41cb41a42fc5a8dc5_5.jpeg",
            "tags": [
                "EdTech"
            ]
            },
            {
            "startup_name": "Planys Technologies",
            "description": "Autonomous underwater vehicle and subsea inspection solutions.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/67c820d7a5246ab393349a11_67c017b76c5f3c51d73322a5_planys-technologies-squarelogo-1558681940014.webp",
            "tags": [
                "Engg"
            ]
            },
            {
            "startup_name": "Tiger Analytics",
            "description": "Advanced analytics and AI consulting for enterprises.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/67c820e886fb7be12e562efc_67c01809ec778c3b7467d272_favicon-Tiger-Analytics_.webp",
            "tags": [
                "Consulting",
                "AI"
            ]
            },
            {
            "startup_name": "Wishup Technologies",
            "description": "Remote assistants and virtual staffing solutions for businesses.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/67777511978a64e0381b372d_66d7fb2eebca15ace2333c88_wishup_services_logo.jpeg",
            "tags": [
                "Consulting"
            ]
            },
            {
            "startup_name": "Zouk",
            "description": "Direct-to-consumer fashion and lifestyle brand from Mumbai.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/67777514167bcd9f7494b182_66f95bb6e9c9fbe56729e835_xouk.jpeg",
            "tags": [
                "D2C"
            ]
            },
            {
            "startup_name": "0xytocin Labs",
            "description": "Blockchain and Web3 product development and innovation lab.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/67777514167bcd9f7494b182_66f95bb6e9c9fbe56729e835_xouk.jpeg",
            "tags": [
                "Internet"
            ]
            },
            {
            "startup_name": "4AM Digital",
            "description": "Digital marketing and advertising agency based in Mumbai.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774db64a7158f3d8ec080_66d7fc1051f4e338a09e5485_1630626216141.jpeg",
            "tags": [
                "Ads/Media"
            ]
            },
            {
            "startup_name": "99x Studio",
            "description": "Product design and UX-focused digital studio in Bengaluru.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774db64a7158f3d8ec07c_67477d1ac5e142b66a3e2de8_99xstartup_logo.jpeg",
            "tags": [
                "Design"
            ]
            },
            {
            "startup_name": "Ashwatta",
            "description": "Sustainable water management and climate resilience solutions provider.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/686c92926178e1b9a1340801_ashwatta_logo.jpg",
            "tags": [
                "ClimateTech"
            ]
            },
            {
            "startup_name": "Cambridge Mobile Telematics",
            "description": "Mobile telematics and insurance analytics using smartphone sensors.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774e4fb1b840b2c09d943_671935dcc49fc05109cee615_cambridge_mobile_telematics_logo.jpeg",
            "tags": [
                "Software"
            ]
            },
            {
            "startup_name": "Eazybe",
            "description": "Enterprise SaaS solutions for business process automation.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774ec64a7158f3d8eca8d_66d7fb3e100260bb86ac6d4f_eazybe_logo.jpeg",
            "tags": [
                "Software",
                "SaaS"
            ]
            },
            {
            "startup_name": "GalaxEye",
            "description": "Spacetech company building satellite and space hardware solutions.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774f064a7158f3d8ecc73_66d7fc8f21ddba530322a496_1695474495454.jpeg",
            "tags": [
                "Space",
                "Manufacturing"
            ]
            },
            {
            "startup_name": "InCore Semiconductors",
            "description": "Semiconductor design house developing analog and power ICs.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/677774f4ea4f6b56dd9cc85f_66d7fb5ebfa3994bd1f55d18_incoresemi_logo.jpeg",
            "tags": [
                "Semicon",
                "Manufacturing"
            ]
            },
            {
            "startup_name": "Pragya Cyber Private Limited",
            "description": "Cybersecurity software and services across India and US.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/686cad56482d52bf6463a938_1701433827859.jpg",
            "tags": [
                "Software"
            ]
            },
            {
            "startup_name": "Riverline",
            "description": "Software company building developer tools and cloud services.",
            "image": "https://cdn.prod.website-files.com/6669fc0ac53c6773c4f2f246/684fffa9d24d0904649acea2_hq3YReZr5F5irph5zcPgbGhD6pI.avif",
            "tags": [
                "Software"
            ]
            }
        ]
        }

    @staticmethod
    def get_social_media(college_id: int) -> dict:
        """Get college social media links"""
        return {
            "official": {
                "facebook": "https://facebook.com/nita.official",
                "twitter": "https://twitter.com/nita_official",
                "instagram": "https://instagram.com/nita.official",
                "youtube": "https://youtube.com/@nita_official",
                "linkedin": "https://linkedin.com/school/nita"
            }
        }

    @staticmethod
    def get_nearby_places(college_id: int) -> dict:
        """Get nearby places information"""
        return {
            "places": [
                {'name': "Elliot's Beach",
                'category': 'Beach',
                'distance': '~6.5 km'},
                {'name': 'Besant Nagar',
                'category': 'Neighbourhood/shoreline',
                'distance': '~5 km'},
                {'name': 'Theosophical Society',
                'category': 'Historic garden/campus',
                'distance': '~3 km'},
                {'name': 'Kalakshetra Foundation',
                'category': 'Cultural academy (dance & crafts)',
                'distance': '~4 km'},
                {'name': 'Phoenix Marketcity',
                'category': 'Shopping mall',
                'distance': '~6 km'},
                {'name': 'Marina Beach',
                'category': 'Beach/landmark',
                'distance': '~8-10 km'},
                {'name': 'Kapaleeshwarar Temple',
                'category': 'Temple',
                'distance': '~7-8 km'},
                {'name': 'Semmozhi Poonga',
                'category': 'Botanical garden',
                'distance': '~5 km'},
                {'name': 'Express Avenue',
                'category': 'Shopping mall',
                'distance': '~8-9 km'},
                {'name': 'Guindy National Park / Snake Park',
                'category': 'Urban national park',
                'distance': '~4 km'}
            ]
        }
