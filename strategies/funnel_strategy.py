"""
Funnel Strategy Module
Generates pricing models, conversion strategies, and funnel designs
"""

def generate_funnel(course_title):
    """Generate course funnel strategy (Free → Paid)"""
    return {
        "funnel_stages": {
            "awareness": {
                "free_content": [
                    f"YouTube: '5 {course_title} mistakes beginners make'",
                    f"Blog: 'Complete {course_title} roadmap'",
                    "Instagram Reels: Quick tips and tricks",
                    "LinkedIn Posts: Industry insights"
                ],
                "lead_magnets": [
                    f"Free eBook: {course_title} Interview Questions",
                    "Free Webinar: Industry trends",
                    "Free Checklist: Learning roadmap",
                    "Free Templates: Resume + Cover letter"
                ]
            },
            
            "interest": {
                "free_trial": "7-day free access to first module",
                "free_workshop": f"Live 2-hour {course_title} workshop",
                "free_community": "Join Telegram community for free tips",
                "email_nurture": "5-day email course"
            },
            
            "decision": {
                "tripwire": "₹99 mini-course (leads to main course)",
                "consultation": "Free 15-min career consultation call",
                "comparison_guide": "TechITFactory vs Others",
                "faq_page": "Address all objections"
            },
            
            "action": {
                "main_course": f"Complete {course_title} Course - ₹2,999",
                "payment_plans": "EMI options available",
                "bonuses": [
                    "Interview prep module",
                    "Resume templates",
                    "LinkedIn optimization guide",
                    "Job referral support"
                ],
                "guarantee": "30-day money-back guarantee"
            },
            
            "retention": {
                "upsells": [
                    "Advanced certification course - ₹4,999",
                    "1-on-1 mentorship - ₹9,999/month",
                    "Job placement premium - ₹14,999"
                ],
                "community": "Lifetime access to alumni network",
                "referral_program": "Refer 3 friends, get 1 month free mentorship"
            }
        },
        
        "conversion_boosters": [
            "Exit intent popup: 10% additional discount",
            "Countdown timer: Creates urgency",
            "Live chat: Instant doubt clearing",
            "Social proof: Show real-time enrollments",
            "Testimonial videos: 3-5 success stories",
            "Money-back guarantee badge: Reduces risk"
        ]
    }


def generate_pricing(course_title):
    """Generate pricing model and discount suggestions"""
    return {
        "pricing_tiers": {
            "basic": {
                "name": "Self-Paced Learning",
                "price": "₹2,999",
                "original_price": "₹9,999",
                "discount": "70% OFF",
                "features": [
                    f"Complete {course_title} course",
                    "Lifetime access",
                    "Community support",
                    "Certificate of completion",
                    "5 hands-on projects"
                ],
                "best_for": "Self-motivated learners"
            },
            
            "pro": {
                "name": "Pro Learning (Most Popular)",
                "price": "₹4,999",
                "original_price": "₹14,999",
                "discount": "67% OFF",
                "features": [
                    "Everything in Basic +",
                    "Live doubt clearing sessions",
                    "Weekly Q&A calls",
                    "Interview preparation",
                    "Resume building assistance",
                    "Job referral support"
                ],
                "best_for": "Serious learners seeking jobs",
                "badge": "RECOMMENDED"
            },
            
            "premium": {
                "name": "Premium + Mentorship",
                "price": "₹9,999",
                "original_price": "₹29,999",
                "discount": "67% OFF",
                "features": [
                    "Everything in Pro +",
                    "1-on-1 mentorship (4 sessions)",
                    "Portfolio review",
                    "Mock interviews (3 rounds)",
                    "LinkedIn profile optimization",
                    "Direct job referrals",
                    "Priority support"
                ],
                "best_for": "Career switchers & serious professionals"
            }
        },
        
        "payment_options": {
            "full_payment": "Pay in full - Get 5% extra discount",
            "emi_3_months": "₹1,000 x 3 months (0% interest)",
            "emi_6_months": "₹550 x 6 months (small processing fee)"
        },
        
        "discount_strategies": {
            "launch_discount": "70% OFF for first 100 students",
            "flash_sale": "48-hour flash sale every month",
            "festival_offers": "Diwali/New Year special - 75% OFF",
            "student_discount": "Extra 10% for college students (ID required)",
            "group_discount": "Enroll with 2 friends, get 15% extra off",
            "referral_discount": "₹500 OFF for each successful referral"
        },
        
        "scarcity_tactics": [
            "Only 50 seats available this batch",
            "Price increases to ₹4,999 after 100 enrollments",
            "Bonus materials available only for first 50 students",
            "Live sessions limited to 30 participants"
        ],
        
        "value_justification": f"""
Compare the investment:
- Regular college course: ₹1,00,000 + 2 years
- Other online courses: ₹15,000 + 6 months
- TechITFactory: ₹2,999 + 30 days ← Best ROI!

After completing this course, average salary increase: ₹3-5 LPA
Your investment pays back in first month of new job! 🚀
"""
    }


def generate_conversion_boosters():
    """Generate specific conversion optimization tactics"""
    return {
        "psychological_triggers": {
            "scarcity": [
                "Only 10 seats left in this batch",
                "Price increases in 48 hours",
                "Bonuses available for first 50 students only",
                "Limited time access to live sessions"
            ],
            
            "urgency": [
                "Countdown timer: 23:59:45",
                "Flash sale ends tonight",
                "Early bird discount expires soon",
                "Join before batch fills up"
            ],
            
            "social_proof": [
                "5,247 students enrolled",
                "Live enrollment ticker",
                "Recent reviews scrolling",
                "Popular choice badge",
                "Featured on [media outlets]"
            ],
            
            "authority": [
                "Certified instructor",
                "10+ years industry experience",
                "Worked at [big companies]",
                "Published author/speaker"
            ],
            
            "reciprocity": [
                "Free resources before asking for sale",
                "Free webinar/workshop",
                "Free consultation call",
                "Free tools/templates"
            ]
        },
        
        "landing_page_elements": {
            "above_the_fold": [
                "Compelling headline",
                "Subheadline with benefit",
                "Hero image/video",
                "Primary CTA button",
                "Trust badges"
            ],
            
            "middle_section": [
                "Problem/Solution statement",
                "Course curriculum",
                "What you'll learn (outcomes)",
                "Social proof (testimonials)",
                "Instructor credibility"
            ],
            
            "bottom_section": [
                "Pricing options",
                "FAQs",
                "Final CTA",
                "Guarantee",
                "Contact information"
            ]
        },
        
        "cta_optimization": {
            "button_text": [
                "❌ Don't: 'Submit', 'Click Here'",
                "✅ Do: 'Enroll Now', 'Start Learning', 'Get Instant Access'",
                "✅ Add value: 'Yes, I Want Job-Ready Skills'",
                "✅ Add urgency: 'Grab My Seat Before It's Gone'"
            ],
            
            "button_design": [
                "Large and prominent",
                "Contrasting color (orange/green)",
                "White space around it",
                "Multiple CTAs throughout page",
                "Sticky CTA button on mobile"
            ]
        },
        
        "mobile_optimization": [
            "Responsive design",
            "Click-to-call button",
            "Easy checkout process",
            "Fast loading (< 2 seconds)",
            "Large tap targets",
            "Simplified forms"
        ],
        
        "exit_intent_strategies": {
            "popup_offer": "Wait! Get 10% OFF Before You Go",
            "lead_capture": "Download Free Guide Instead",
            "chat_trigger": "Have questions? Let's chat!",
            "reminder": "Save Your Spot - Limited Seats Available"
        },
        
        "retargeting_tactics": [
            "Facebook/Instagram pixel installed",
            "Show testimonials to cart abandoners",
            "Offer discount to repeat visitors",
            "Email sequence for non-converters",
            "WhatsApp remarketing messages"
        ],
        
        "marketing_audit_checklist": {
            "landing_page": [
                "❓ Is headline clear and benefit-focused?",
                "❓ Are CTAs prominent and action-oriented?",
                "❓ Testimonials, ratings, student count visible?",
                "❓ Scarcity or urgency elements present?",
                "❓ Mobile-friendly design?",
                "❓ Page loads in < 3 seconds?",
                "❓ Guarantees, certifications, secure payment?"
            ],
            "immediate_fixes": [
                "✅ Add countdown timer for urgency",
                "✅ Make CTA button bigger and orange",
                "✅ Add 3-5 video testimonials above the fold",
                "✅ Optimize images (compress for faster loading)",
                "✅ Add live chat widget",
                "✅ Create exit-intent popup with 10% discount",
                "✅ Add trust badges (payment security, guarantee)",
                "✅ Set up email automation sequence"
            ]
        }
    }
