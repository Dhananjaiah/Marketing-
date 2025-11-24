"""
Growth Planner Module
Generates 30-day plans, content calendars, influencer strategies, and community building
"""

# Default course pricing for revenue calculations
DEFAULT_COURSE_PRICE = 2999

def generate_30_day_plan(course_title, course_price=None):
    """Generate detailed 30-day growth plan"""
    # Use provided price or default
    price = course_price if course_price else DEFAULT_COURSE_PRICE
    
    return {
        "week_1": {
            "focus": "Awareness Building",
            "goals": {
                "reach": "1000+ people",
                "leads": "50+ email signups",
                "conversions": "5+ enrollments",
                "revenue": f"₹{price * 5:,}+"
            },
            "daily_tasks": {
                "monday": ["Create YouTube video", "Design 5 Instagram posts", "Write blog post"],
                "tuesday": ["Post on LinkedIn", "Share in relevant groups", "Email existing list"],
                "wednesday": ["Instagram Reels (3)", "Twitter thread", "WhatsApp status"],
                "thursday": ["YouTube Shorts (5)", "Facebook posts", "Update landing page"],
                "friday": ["LinkedIn article", "Instagram carousel", "Email follow-up"],
                "saturday": ["Community engagement", "Reply to comments", "DMs"],
                "sunday": ["Plan next week", "Analyze metrics", "Content batch creation"]
            },
            "metrics_to_track": [
                "Social media reach & engagement",
                "Website traffic",
                "Email open rates",
                "Landing page views",
                "Time on page"
            ]
        },
        
        "week_2": {
            "focus": "Lead Generation",
            "goals": {
                "reach": "2000+ people",
                "leads": "100+ email signups",
                "conversions": "10+ enrollments",
                "revenue": f"₹{price * 10:,}+"
            },
            "daily_tasks": {
                "monday": ["Launch lead magnet", "Create landing page", "Set up email automation"],
                "tuesday": ["Run Facebook ads", "Google ads campaign", "Instagram ads"],
                "wednesday": ["Host live webinar", "Q&A session", "Collect emails"],
                "thursday": ["Follow up with leads", "Send free resources", "WhatsApp outreach"],
                "friday": ["Collaborate with influencer", "Guest posts", "Podcast interview"],
                "saturday": ["Engage with community", "Answer queries", "Build trust"],
                "sunday": ["Review conversion rates", "Optimize campaigns", "Plan week 3"]
            },
            "metrics_to_track": [
                "Lead magnet downloads",
                "Email list growth",
                "Ad performance (CTR, CPC)",
                "Webinar attendance",
                "Cost per lead"
            ]
        },
        
        "week_3": {
            "focus": "Conversion Optimization",
            "goals": {
                "reach": "3000+ people",
                "leads": "150+ email signups",
                "conversions": "15+ enrollments",
                "revenue": f"₹{price * 15:,}+"
            },
            "daily_tasks": {
                "monday": ["Email sequence Day 1", "Retargeting ads", "Case studies"],
                "tuesday": ["Limited time offer", "Scarcity emails", "WhatsApp broadcast"],
                "wednesday": ["Testimonial collection", "Social proof", "Success stories"],
                "thursday": ["Flash sale announcement", "Push notifications", "SMS campaign"],
                "friday": ["Personal outreach", "Sales calls", "Deal closing"],
                "saturday": ["Follow up non-converters", "Objection handling", "Special offers"],
                "sunday": ["Review sales data", "Identify bottlenecks", "Plan week 4"]
            },
            "metrics_to_track": [
                "Email-to-sale conversion",
                "Cart abandonment rate",
                "Average order value",
                "Sales call success rate",
                "ROI on ads"
            ]
        },
        
        "week_4": {
            "focus": "Scale & Optimize",
            "goals": {
                "reach": "4000+ people",
                "leads": "200+ email signups",
                "conversions": "20+ enrollments",
                "revenue": f"₹{price * 20:,}+"
            },
            "daily_tasks": {
                "monday": ["Scale winning ads", "Increase budget", "New audiences"],
                "tuesday": ["Partner with more influencers", "Affiliate program", "Referrals"],
                "wednesday": ["Optimize landing page", "A/B testing", "Improve conversion"],
                "thursday": ["Launch upsells", "Bundle offers", "Premium tier promotion"],
                "friday": ["Build community", "Onboard students", "Collect feedback"],
                "saturday": ["Create success stories", "Video testimonials", "Case studies"],
                "sunday": ["Month review", "ROI calculation", "Plan next month"]
            },
            "metrics_to_track": [
                "Overall ROI",
                "Customer acquisition cost",
                "Lifetime value",
                "Referral rate",
                "Student satisfaction score"
            ]
        },
        
        "success_criteria": {
            "minimum": f"30 enrollments in 30 days (₹{price * 30:,} revenue)",
            "target": f"50 enrollments in 30 days (₹{price * 50:,} revenue)",
            "stretch": f"100 enrollments in 30 days (₹{price * 100:,} revenue)"
        },
        
        "budget_allocation": {
            "paid_ads": "₹20,000 (40%)",
            "influencer_marketing": "₹15,000 (30%)",
            "content_creation": "₹10,000 (20%)",
            "tools_and_software": "₹5,000 (10%)",
            "total": "₹50,000"
        }
    }


def generate_content_calendar(course_title):
    """Generate daily content calendar"""
    return {
        "content_types": {
            "monday": {
                "platform": "YouTube",
                "format": "Long-form tutorial (15-20 min)",
                "topic": f"{course_title} tutorial or case study",
                "goal": "Establish authority & drive traffic",
                "posting_time": "6:00 PM IST (After office hours)"
            },
            
            "tuesday": {
                "platform": "LinkedIn",
                "format": "Professional post + carousel",
                "topic": "Industry insights or career tips",
                "goal": "B2B networking & professional credibility",
                "posting_time": "9:00 AM IST (Morning commute)"
            },
            
            "wednesday": {
                "platform": "Instagram",
                "format": "3 Reels",
                "topic": f"Quick {course_title} tips, memes, before/after",
                "goal": "Viral reach & engagement",
                "posting_time": "8:00 PM IST (Peak engagement)"
            },
            
            "thursday": {
                "platform": "Email",
                "format": "Newsletter + promotional content",
                "topic": "Course update + success story + CTA",
                "goal": "Nurture leads & conversions",
                "posting_time": "7:00 AM IST (Morning read)"
            },
            
            "friday": {
                "platform": "Twitter",
                "format": "Thread (8-10 tweets)",
                "topic": f"{course_title} tips, roadmap, resources",
                "goal": "Thought leadership & shareability",
                "posting_time": "1:00 PM IST (Lunch break)"
            },
            
            "saturday": {
                "platform": "WhatsApp/Telegram",
                "format": "Community engagement + live Q&A",
                "topic": "Answer doubts, share tips, motivate",
                "goal": "Build community & trust",
                "posting_time": "8:00 PM IST (Evening free time)"
            },
            
            "sunday": {
                "platform": "Blog",
                "format": "Long-form article (2000+ words)",
                "topic": f"Comprehensive {course_title} guide",
                "goal": "SEO & evergreen content",
                "posting_time": "10:00 AM IST (Sunday morning)"
            }
        },
        
        "content_themes_by_week": {
            "week_1": "Introduction & Fundamentals",
            "week_2": "Common Mistakes & Solutions",
            "week_3": "Success Stories & Case Studies",
            "week_4": "Advanced Tips & Career Guidance"
        },
        
        "hashtag_strategy": {
            "high_volume": ["#DevOps", "#Kubernetes", "#MLOps", "#CloudComputing", "#TechCareers"],
            "medium_volume": [f"#{course_title.replace(' ', '')}", "#LearnDevOps", "#TechEducation", "#IndianDevelopers"],
            "branded": ["#TechITFactory", "#TeluguTech", "#LearnInTelugu"],
            "mix_formula": "2 high + 3 medium + 2 branded + 3 niche = 10 hashtags per post"
        },
        
        "content_ideas": {
            "educational": [
                f"5 {course_title} concepts explained simply",
                "Step-by-step project walkthrough",
                "Common interview questions answered",
                "Best practices and tips",
                "Tool comparisons and recommendations"
            ],
            "inspirational": [
                "Student success stories",
                "Career transformation journeys",
                "Day in the life of a DevOps engineer",
                "Salary progression stories",
                "Overcoming learning challenges"
            ],
            "promotional": [
                "Course features and benefits",
                "Limited time offers",
                "Behind the scenes content",
                "Free resource announcements",
                "Live session invitations"
            ],
            "engagement": [
                "Polls and questions",
                "Challenge participants",
                "Ask me anything sessions",
                "Community spotlights",
                "Memes and relatable content"
            ]
        }
    }


def generate_influencer_strategy(course_title):
    """Generate influencer outreach and collaboration plan"""
    return {
        "target_influencers": {
            "tier_1_micro": {
                "followers": "10K - 50K",
                "platforms": ["Instagram", "YouTube", "LinkedIn"],
                "niche": "DevOps, Cloud, Tech Education",
                "budget_per_post": "₹5,000 - ₹15,000",
                "expected_roi": "5-10 enrollments per collaboration",
                "target_number": "10 influencers",
                "examples": [
                    "Telugu tech YouTubers",
                    "DevOps bloggers",
                    "Coding instructors on Instagram"
                ]
            },
            
            "tier_2_mid": {
                "followers": "50K - 200K",
                "platforms": ["YouTube", "LinkedIn"],
                "niche": "Tech Careers, Software Development",
                "budget_per_post": "₹20,000 - ₹50,000",
                "expected_roi": "15-30 enrollments per collaboration",
                "target_number": "3-5 influencers",
                "examples": [
                    "Popular tech YouTube channels",
                    "LinkedIn tech influencers",
                    "Tech career coaches"
                ]
            },
            
            "tier_3_affiliate": {
                "followers": "Any",
                "model": "Commission-based (30% per sale)",
                "platforms": ["All"],
                "commission": "₹900 per enrollment",
                "target_number": "50 affiliates in 30 days",
                "recruitment": "Open affiliate program with easy signup"
            }
        },
        
        "outreach_templates": {
            "email_subject": f"Collaboration Opportunity - {course_title} Course",
            "email_body": f"""
Hi {{{{name}}}},

I'm Dhananjai from TechITFactory. I've been following your content on {{{{platform}}}} and love how you explain {{{{topic}}}}.

We've just launched a {course_title} course specifically for Indian learners with Telugu support. 5000+ students have already enrolled.

I'd love to collaborate with you:

Option 1: Sponsored content (₹{{{{amount}}}})
- 1 dedicated video/post about our course
- Your honest review
- Promo code for your audience (20% discount)

Option 2: Affiliate partnership (30% commission)
- ₹900 per enrollment through your link
- No upfront cost
- Complete creative freedom

We can also give you free course access to review.

Interested? Let's chat!

Best regards,
Dhananjai
TechITFactory
+91-XXXXXXXXXX
""",
            
            "dm_template": f"""
Hey [Name]! 👋

Love your content on {{{{topic}}}}!

Quick question: Do you collaborate with EdTech brands?

We have a {course_title} course for Indian learners and would love to partner.

Can we chat? 🚀
""",
            
            "follow_up": """
Hi [Name],

Following up on my previous message about collaboration.

We're currently working with [Influencer X] and [Influencer Y], and the response has been amazing!

Would you be open to a quick 10-min call to discuss?

Thanks!
"""
        },
        
        "collaboration_types": [
            {
                "type": "Dedicated Video/Post",
                "deliverable": "1 YouTube video or Instagram post",
                "timeline": "1 week",
                "cost": "₹10,000 - ₹50,000",
                "requirements": "Honest review, call-to-action, promo code mention"
            },
            {
                "type": "Course Review",
                "deliverable": "Honest review after completing the course",
                "timeline": "2 weeks",
                "cost": "Free course access + ₹5,000",
                "requirements": "Complete at least 50% of course, genuine feedback"
            },
            {
                "type": "Affiliate Marketing",
                "deliverable": "Ongoing promotion with unique link",
                "timeline": "Continuous",
                "cost": "30% commission per sale (₹900)",
                "requirements": "Regular promotion, track conversions"
            },
            {
                "type": "Guest Appearance",
                "deliverable": "Live session or interview",
                "timeline": "1 day",
                "cost": "₹15,000 + free course",
                "requirements": "1-hour live session, Q&A with students"
            },
            {
                "type": "Bundle Collaboration",
                "deliverable": "Create joint course/resource",
                "timeline": "1 month",
                "cost": "Revenue share 50-50",
                "requirements": "Both parties contribute content, joint marketing"
            }
        ],
        
        "tracking_metrics": [
            "Promo code usage by influencer",
            "Affiliate link clicks and conversions",
            "Traffic from influencer posts",
            "Cost per acquisition per influencer",
            "ROI per collaboration",
            "Engagement rate on influencer content"
        ],
        
        "success_checklist": [
            "✅ Research and identify 20+ potential influencers",
            "✅ Create outreach spreadsheet with contact info",
            "✅ Send personalized outreach messages",
            "✅ Follow up within 3-5 days",
            "✅ Negotiate terms and finalize agreement",
            "✅ Provide course access and promotional materials",
            "✅ Track performance and calculate ROI",
            "✅ Maintain relationship for future collaborations"
        ]
    }


def generate_community_strategy(course_title):
    """Generate community building and engagement strategy"""
    return {
        "community_platforms": {
            "telegram": {
                "primary_group": f"TechITFactory {course_title} Students",
                "purpose": "Daily tips, doubt clearing, networking",
                "moderation": "24/7 support team + AI bot",
                "activities": [
                    "Daily tip of the day (9 AM)",
                    "Weekly coding challenges (Monday)",
                    "Monthly contests with prizes",
                    "Success story sharing (Friday)",
                    "Job posting alerts (Real-time)"
                ],
                "rules": [
                    "No spam or self-promotion",
                    "Be respectful and helpful",
                    "Ask questions freely",
                    "Share knowledge",
                    "Support fellow learners"
                ]
            },
            
            "whatsapp": {
                "broadcast_list": "Announcements & updates (one-way)",
                "study_groups": "Max 256 per group, create multiple batches",
                "vip_group": "Premium students only with exclusive content",
                "alumni_group": "Course graduates for networking and referrals"
            },
            
            "discord": {
                "text_channels": [
                    "#introductions - Welcome new members",
                    "#general-discussion - Casual chat",
                    "#help-and-support - Ask questions",
                    "#project-showcase - Share your work",
                    "#job-opportunities - Job postings",
                    "#resources - Useful links and tools",
                    "#telugu-corner - Telugu language support",
                    "#announcements - Official updates"
                ],
                "voice_channels": [
                    "Study Together - Co-working sessions",
                    "Live Q&A - Weekly doubt clearing",
                    "Mock Interviews - Practice sessions",
                    "Networking - Casual hangouts"
                ],
                "roles": [
                    "👑 Admin",
                    "🎓 Mentor",
                    "⭐ Pro Member",
                    "👤 Student",
                    "🎉 Alumni"
                ]
            },
            
            "linkedin_group": {
                "name": f"TechITFactory {course_title} Professionals",
                "purpose": "Professional networking & job referrals",
                "content_strategy": "Industry news, career tips, alumni success stories",
                "posting_frequency": "3-4 posts per week"
            }
        },
        
        "engagement_activities": {
            "daily": [
                "Morning motivation message (7 AM)",
                "Tip of the day (9 AM)",
                "Answer 10+ questions throughout the day",
                "Share interesting article/video (6 PM)",
                "Evening checkpoint (9 PM)"
            ],
            
            "weekly": [
                "Monday: Coding challenge announcement",
                "Tuesday: Live Q&A session (7 PM, 1 hour)",
                "Wednesday: Student spotlight feature",
                "Thursday: Industry news roundup",
                "Friday: Success story of the week",
                "Saturday: Weekend workshop or webinar",
                "Sunday: Plan your week session"
            ],
            
            "monthly": [
                "Guest speaker session (Industry expert)",
                "Virtual networking event",
                "Hackathon or project competition",
                "Alumni meetup (online/offline)",
                "Community awards and recognition"
            ]
        },
        
        "gamification": {
            "points_system": {
                "complete_module": "10 points",
                "help_another_student": "5 points",
                "attend_live_session": "15 points",
                "complete_project": "25 points",
                "share_success_story": "20 points",
                "refer_a_friend": "30 points",
                "win_challenge": "50 points",
                "get_job_offer": "100 points"
            },
            
            "leaderboard": {
                "update_frequency": "Weekly",
                "display": "Top 10 students",
                "categories": ["Overall", "This Week", "This Month"],
                "visibility": "Public in community"
            },
            
            "badges": [
                "🚀 Early Bird - Complete Module 1 in 3 days",
                "💪 Consistent Learner - Login 7 days straight",
                "🎯 Project Master - Complete all projects",
                "🤝 Community Helper - Help 10 students",
                "⭐ Star Performer - Top 10 on leaderboard",
                "🏆 Course Completer - Finish entire course",
                "💼 Job Winner - Get job offer"
            ],
            
            "rewards": {
                "100_points": "TechITFactory T-shirt + Stickers",
                "250_points": "Free advanced mini-course",
                "500_points": "1-month free mentorship",
                "1000_points": "Lifetime premium access + Certificate of Excellence",
                "referral_bonus": "₹500 OFF on next course per referral"
            }
        },
        
        "moderation_guidelines": {
            "response_time": "< 2 hours for questions",
            "escalation": "Complex issues to senior mentors",
            "content_policy": "Remove spam, offensive content immediately",
            "positive_reinforcement": "Celebrate wins, encourage struggling students",
            "conflict_resolution": "Address conflicts privately, maintain peace"
        },
        
        "success_metrics": {
            "engagement": [
                "Daily active users (DAU) - Target: 60%",
                "Messages per day - Target: 100+",
                "Average response time - Target: < 2 hours",
                "Member satisfaction score - Target: 4.5/5"
            ],
            "retention": [
                "Course completion rate - Target: 70%",
                "Community retention (30 days) - Target: 80%",
                "Referral rate - Target: 20%"
            ],
            "outcomes": [
                "Job placement rate - Target: 85%",
                "Average time to job - Target: 90 days",
                "Salary increase - Target: ₹3-5 LPA"
            ]
        }
    }
