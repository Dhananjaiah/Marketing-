"""
Content Generator Module
Generates all marketing content including landing pages, ads, SEO, emails, etc.
"""

def generate_landing_page(course_title):
    """Generate high-converting landing page content"""
    return {
        "headline": f"Master {course_title} in 30 Days - Guaranteed Job-Ready Skills",
        "subheadline": f"Join 5000+ Telugu Students Who Transformed Their Career with TechITFactory",
        
        "hero_section": {
            "hook": f"🚀 Want to become a {course_title} expert without wasting months?",
            "promise": "Learn industry-proven techniques from real-world projects",
            "cta_primary": "Enroll Now at ₹2,999 (Limited Seats!)",
            "cta_secondary": "Download Free Course Outline"
        },
        
        "benefits": [
            "✅ 100% Hands-on Projects (No Theory Overload)",
            "✅ Live Doubt Clearing Sessions in Telugu + English",
            "✅ Interview Preparation & Resume Building",
            "✅ Lifetime Access to Course Updates",
            "✅ Certificate of Completion",
            "✅ Direct WhatsApp Support Group"
        ],
        
        "social_proof": {
            "testimonial_1": '"Nenu 3 months lo DevOps engineer ga job dorikindi. TechITFactory content chala practical!" - Ramesh, Hyderabad',
            "testimonial_2": '"Best investment for my career. Projects real-time scenarios tho chala helpful!" - Priya, Bangalore',
            "stats": "5000+ Students | 4.8★ Rating | 85% Job Placement"
        },
        
        "urgency_section": {
            "title": "⏰ Limited Time Offer - Ends in 48 Hours!",
            "original_price": "₹9,999",
            "discounted_price": "₹2,999",
            "savings": "₹7,000 OFF (70% Discount)",
            "bonus": "🎁 Free: Interview Questions eBook + Resume Templates"
        },
        
        "curriculum_highlights": [
            f"Module 1: {course_title} Fundamentals (Beginner Friendly)",
            "Module 2: Real-World Industry Projects",
            "Module 3: Advanced Techniques & Best Practices",
            "Module 4: Interview Preparation & Mock Tests"
        ],
        
        "faq": [
            {
                "q": "Telugu lo doubt clear cheyyagalara?",
                "a": "Yes! Live sessions lo Telugu + English rendu languages lo support untundi."
            },
            {
                "q": "Job guarantee unda?",
                "a": "We provide 100% interview preparation and placement guidance. 85% of our students get placed within 3 months."
            },
            {
                "q": "Prerequisites emaina unavaya?",
                "a": "Basic computer knowledge chalu. We teach everything from scratch."
            }
        ],
        
        "final_cta": {
            "headline": "🔥 Don't Miss This Opportunity - Join Today!",
            "button": "Yes, I Want Job-Ready Skills →",
            "guarantee": "💯 30-Day Money-Back Guarantee"
        }
    }


def generate_ad_scripts(course_title):
    """Generate YouTube + Instagram ad scripts in Telugu and English"""
    return {
        "youtube_ads": {
            "english": {
                "hook_5sec": f"Want to master {course_title} and get hired in 90 days?",
                "script_30sec": f"""
[0-5s] Struggling to break into {course_title}? You're not alone.
[5-15s] TechITFactory has trained 5000+ students with 100% hands-on projects.
[15-25s] Real-world scenarios, Telugu support, and interview prep included.
[25-30s] Limited seats at ₹2,999. Enroll now at members.techitfactory.com
""",
                "script_60sec": f"""
[0-10s] Hi! Are you trying to learn {course_title} but feeling overwhelmed by too much theory?
[10-25s] I'm from TechITFactory, and we've helped 5000+ Telugu students land DevOps jobs. Our secret? 100% practical learning with real projects.
[25-40s] You'll build actual industry projects, get live doubt clearing in Telugu, and receive complete interview preparation.
[40-50s] For the next 48 hours, we're offering 70% OFF - just ₹2,999 instead of ₹9,999.
[50-60s] Visit members.techitfactory.com now. Limited seats available. Your dream job is just one click away!
"""
            },
            "telugu": {
                "hook_5sec": f"{course_title} nerchukovdaniki ready ga unnara?",
                "script_30sec": f"""
[0-5s] {course_title} career start cheyyali anukuntunnara?
[5-15s] TechITFactory lo 5000+ students trained ayyaru, 100% practical projects tho.
[15-25s] Telugu lo support, real projects, interview preparation - anni include.
[25-30s] ₹2,999 lo enroll avvandi. members.techitfactory.com ki vellandi.
""",
                "script_60sec": f"""
[0-10s] Namaste! {course_title} nerchukovadam chala kastam ga anipistondi? Theory ekkuva, practical takkuva?
[10-25s] Nenu TechITFactory nundi. Memu 5000+ Telugu students ki DevOps jobs rakunda help chesam. Maadi 100% practical learning.
[25-40s] Meeru real industry projects build chestaru, Telugu lo doubts clear chestam, complete interview preparation kuda untundi.
[40-50s] Ippudu 48 hours varaku 70% discount - ₹9,999 ki badulu ₹2,999 mathrame.
[50-60s] Ippude members.techitfactory.com visit cheyandi. Limited seats. Mee dream job oka click dooram lo undi!
"""
            }
        },
        
        "instagram_ads": {
            "english": {
                "reel_15sec": f"""
[Visual: Before/After transformation]
Text Overlay: "Me trying to learn {course_title} from YouTube"
[Switch] "Me after TechITFactory course"
[Show: Job offer letter]
Caption: 90 days. Real projects. ₹2,999 only.
""",
                "carousel": [
                    "Slide 1: Tired of tutorial hell? 😫",
                    f"Slide 2: Learn {course_title} the RIGHT way 💡",
                    "Slide 3: 100% Hands-on Projects 🚀",
                    "Slide 4: Telugu + English Support 🙌",
                    "Slide 5: ₹2,999 (70% OFF) ⚡",
                    "Slide 6: Swipe up to enroll! 👆"
                ]
            },
            "telugu": {
                "reel_15sec": f"""
[Visual: Struggle animation]
Text: "YouTube nundi {course_title} nerchukunna nenu"
[Switch] "TechITFactory tarvatha nenu"
[Show: Job offer]
Caption: 90 days lo job. ₹2,999 mathrame.
""",
                "carousel": [
                    "Slide 1: YouTube tutorials tho bore aipoyara? 😫",
                    f"Slide 2: {course_title} correct ga nerchukondi 💡",
                    "Slide 3: 100% Practical Projects 🚀",
                    "Slide 4: Telugu Support Available 🙌",
                    "Slide 5: ₹2,999 discount price ⚡",
                    "Slide 6: Link click cheyandi! 👆"
                ]
            }
        }
    }


def generate_seo_content(course_title):
    """Generate SEO titles, descriptions, and keywords"""
    return {
        "page_title": f"{course_title} Course in Telugu - TechITFactory | Hands-on Training",
        "meta_description": f"Learn {course_title} with 100% practical projects. Telugu + English support. 5000+ students trained. ₹2,999 only. Interview prep included. Enroll now!",
        
        "keywords": {
            "primary": [
                f"{course_title.lower()} course",
                f"{course_title.lower()} training",
                f"{course_title.lower()} tutorial telugu"
            ],
            "secondary": [
                f"learn {course_title.lower()} online",
                f"{course_title.lower()} course in hyderabad",
                f"{course_title.lower()} training in telugu",
                "devops course telugu",
                "techitfactory courses",
                f"{course_title.lower()} for beginners",
                f"{course_title.lower()} certification"
            ],
            "long_tail": [
                f"best {course_title.lower()} course for beginners in india",
                f"how to learn {course_title.lower()} in telugu",
                f"{course_title.lower()} online training with projects",
                f"affordable {course_title.lower()} course for students",
                f"{course_title.lower()} interview preparation telugu"
            ]
        },
        
        "h1": f"Complete {course_title} Course - Master Real-World Projects in 30 Days",
        "h2_tags": [
            "Why Choose TechITFactory for DevOps Training?",
            f"What You'll Learn in This {course_title} Course",
            "Course Curriculum & Project Details",
            "Student Success Stories & Testimonials",
            "Pricing & Enrollment Information"
        ],
        
        "blog_titles": [
            f"Top 10 {course_title} Skills Every Developer Needs in 2025",
            f"How I Became a {course_title} Engineer in 90 Days (Telugu Guide)",
            f"{course_title} vs Traditional IT: Which Career Path is Better?",
            f"5 Common {course_title} Mistakes Beginners Make (And How to Avoid Them)",
            f"Complete {course_title} Roadmap for Indian Students"
        ]
    }


def generate_sales_copy(course_title):
    """Generate Hook + Story + CTA sales copy"""
    return {
        "short_form": {
            "hook": f"🔥 {course_title} skills kosam months waste chestunnara?",
            "story": "30 days lo real-world projects tho industry-ready avvandi. 5000+ students already transformed their careers.",
            "cta": "Ippude ₹2,999 ki enroll avvandi → members.techitfactory.com"
        },
        
        "long_form": f"""
🎯 HOOK:
Picture this: You spend 6 months watching YouTube tutorials, reading blogs, and trying to learn {course_title}. 
But when you apply for jobs, you still feel unprepared. Sound familiar?

📖 STORY:
Meet Rajesh from Hyderabad. He spent 8 months trying to learn DevOps from free resources. 
Zero confidence. Zero job offers.

Then he joined TechITFactory. In just 30 days:
✅ Completed 5 real-world projects
✅ Cleared 12 technical interviews
✅ Got 3 job offers
✅ Now earning ₹8 LPA

The difference? We don't teach theory. We build projects.

Every single day, you'll work on actual industry scenarios. You'll make mistakes, debug issues, 
and learn exactly how professionals work. Telugu lo doubts clear kar sakte ho. 
Live sessions hai. Interview preparation hai. Resume building hai.

5000+ students have already transformed their careers. Priya got hired in 45 days. 
Suresh increased his salary by 150%. Lakshmi switched from testing to DevOps.

🚀 CTA:
Tumhara number next! But seats limited hai.

Right now, we're offering 70% OFF - just ₹2,999 instead of ₹9,999.
+ Free Interview Questions eBook
+ Free Resume Templates
+ Lifetime Course Access
+ 30-Day Money-Back Guarantee

⏰ Offer expires in 48 hours.

Click here to enroll: members.techitfactory.com

Don't let another month pass watching tutorials. Start building real projects today.

Your dream job is waiting. 🎯
""",
        
        "email_subject_lines": [
            f"🔥 Learn {course_title} in 30 days (Not 6 months)",
            "❌ Stop wasting time on YouTube tutorials",
            "✅ This is how 5000+ students got DevOps jobs",
            f"⚡ {course_title} at ₹2,999 - Last 48 hours",
            "🎁 Free: Interview Questions for DevOps Engineers"
        ]
    }


def generate_email_sequence(course_title):
    """Generate 7-day email sequence"""
    return {
        "day_0": {
            "subject": f"🎉 Welcome to {course_title} Mastery!",
            "preview": "Your journey starts now...",
            "body": f"""
Hi {{{{name}}}},

Welcome to TechITFactory! You've made an excellent decision.

🎯 Here's your roadmap for the next 7 days:

Day 1-2: Master the fundamentals
Day 3-4: Build your first project
Day 5-6: Advanced techniques
Day 7: Interview preparation

📚 Your course access: members.techitfactory.com
Login: {{{{email}}}}
Password: {{{{temp_password}}}}

👉 ACTION ITEM: Login now and watch the welcome video (5 minutes)

Any questions? Just hit reply.

Cheers,
Dhananjai
Founder, TechITFactory

P.S. Join our WhatsApp group for instant doubt clearing: [link]
"""
        },
        
        "day_1": {
            "subject": "✅ Day 1: Let's build your first project!",
            "preview": "Ready to get your hands dirty?",
            "body": f"""
Hey {{{{name}}}},

Ready to get your hands dirty? 💪

Today's goal: Complete Module 1 and start your first project.

📌 What you'll learn:
- {course_title} fundamentals
- Setting up your environment
- Your first hands-on lab

⏰ Time needed: 2-3 hours

👉 Start here: [direct link to Module 1]

Stuck somewhere? Our community is here to help!

Happy learning,
Team TechITFactory
"""
        },
        
        "day_3": {
            "subject": "🔥 You're in the top 30%! Keep going...",
            "preview": "Impressive progress!",
            "body": f"""
{{{{name}}}}, impressive progress! 🎉

You've completed more than 70% of students who start.

Quick check-in:
✅ Completed Module 1? 
✅ Started first project?
✅ Any doubts so far?

💡 Pro tip: Don't aim for perfection. Aim for progress.

Tomorrow: We'll dive into real-world scenarios that companies actually use.

📞 Need help? Book a 1-on-1 call: [calendar link]

Keep crushing it!
Dhananjai
"""
        },
        
        "day_5": {
            "subject": "🎯 Resume tip + Interview question",
            "preview": "Let's talk about getting hired!",
            "body": f"""
Hi {{{{name}}}},

Let's talk about getting hired! 💼

Here's a common interview question:
"Explain the difference between Docker and Kubernetes..."

[Detailed answer with explanation]

📄 Also, I've attached:
- Resume template for {course_title} professionals
- Top 50 interview questions PDF
- Salary negotiation guide

Use these to stand out! ✨

Next: Module 3 unlocks tomorrow. Get ready for advanced concepts!

Best,
Team TechITFactory
"""
        },
        
        "day_7": {
            "subject": "🚀 1 Week Done! Here's what's next...",
            "preview": "Congratulations on completing Week 1!",
            "body": f"""
{{{{name}}}}, congratulations! 🎊

You've completed Week 1. That's a huge milestone!

📊 Your progress:
- Modules completed: {{{{modules_completed}}}}
- Projects built: {{{{projects_completed}}}}
- Doubt sessions attended: {{{{sessions_attended}}}}

🎯 Week 2 Preview:
- Advanced {course_title} techniques
- Industry best practices
- Mock interview session

💬 Quick favor: How's the course so far? Reply with one word.

Also, we'd love to feature your success story. Interested?

Keep up the momentum! 🔥

Cheers,
Dhananjai

P.S. Refer a friend and get 1 month free access to our advanced course!
"""
        }
    }


def generate_automation_messages(course_title):
    """Generate WhatsApp + Telegram automation messages"""
    return {
        "whatsapp": {
            "welcome_message": f"""
🙏 Welcome to TechITFactory!

Congratulations on taking the first step towards mastering {course_title}! 🎉

Here's what happens next:
1️⃣ Access your course: members.techitfactory.com
2️⃣ Join our Telegram group: [link]
3️⃣ Download course materials: [link]

💡 Pro Tip: Start with Module 1 today and complete the first project this week!

Any doubts? Just reply to this message. We're here to help! 🚀

- Team TechITFactory
""",
            "day_3_followup": f"""
Hi {{{{name}}}}! 👋

3 days lo ela undi course? Progress bagunda?

Quick reminder:
✅ Complete first project by day 7
✅ Ask doubts in Telegram group
✅ Watch live session tomorrow 7 PM

Stuck anywhere? Reply "HELP" and we'll schedule a call.

Keep learning! 💪
""",
            "day_7_motivation": f"""
🎉 1 week complete! Great progress {{{{name}}}}!

You're now in the top 20% who actually finish what they start.

Next milestone: Complete Module 2 by day 14

🔥 Bonus tip: Share your project on LinkedIn to build your portfolio!

Need help? We're just a message away.
""",
            "abandoned_cart": f"""
Hey {{{{name}}}}! 👋

We noticed you were interested in our {course_title} course but didn't complete enrollment.

Kuch doubt hai? Let us help!

📞 Call us: +91-XXXXXXXXXX
💬 Reply here with your questions

P.S. Your 70% discount is still valid for next 24 hours! ⏰
"""
        },
        
        "telegram": {
            "welcome_broadcast": f"""
🎊 New Member Alert!

Welcome {{{{name}}}} to TechITFactory {course_title} Batch!

👥 You're now part of 5000+ learner community
📚 Access all resources: /resources
❓ Ask doubts: Just type your question
🎥 Live sessions: Every Tue/Thu 7 PM

Let's start learning! 🚀
""",
            "daily_tip": f"""
💡 Daily {course_title} Tip #{{{{day}}}}:

{{{{tip_content}}}}

💬 Questions? Ask in the group!
🎯 Today's challenge: {{{{challenge}}}}

Keep building! 💪
""",
            "live_session_reminder": f"""
🔴 LIVE SESSION ALERT 🔴

Topic: {{{{topic}}}}
Time: {{{{time}}}}
Link: {{{{link}}}}

Set your reminder! Don't miss this. 🎯

See you there! 👋
"""
        }
    }


def generate_visual_content(course_title):
    """Generate thumbnail ideas and Canva prompts"""
    return {
        "thumbnail_ideas": [
            f"{course_title}\nIN 30 DAYS\n₹2,999 ONLY",
            f"MASTER\n{course_title}\n100% PRACTICAL",
            f"GET HIRED IN\n90 DAYS\n{course_title} COURSE",
            f"5000+ STUDENTS\nTRANSFORMED\nJOIN NOW",
            f"TELUGU + ENGLISH\n{course_title}\nTECHITFACTORY",
            f"70% OFF\n{course_title}\nLIMITED SEATS",
            f"STOP WATCHING\nYOUTUBE\nSTART BUILDING",
            f"₹2,999\n{course_title}\nJOB READY",
            f"FREE\nINTERVIEW PREP\nWITH COURSE",
            f"REAL PROJECTS\nREAL JOBS\n{course_title}"
        ],
        
        "canva_prompts": [
            {
                "type": "Course Announcement",
                "prompt": f"""
Create a vibrant Instagram post:
- Title: "{course_title} Course Now Open!"
- Tagline: "100% Hands-on | Telugu Support"
- Price: ₹2,999 (crossed: ₹9,999)
- CTA Button: "Enroll Now"
- Colors: Orange, Blue, White
- Include: TechITFactory logo, 5-star rating
- Style: Modern, Professional, Energetic
"""
            },
            {
                "type": "Student Testimonial",
                "prompt": f"""
Create a testimonial card:
- Quote: "Best decision for my career!"
- Student: Name + Photo + Job Title
- Course: {course_title}
- Rating: 5 stars
- Background: Gradient (purple to blue)
- Include: Before/After salary comparison
"""
            },
            {
                "type": "Course Features",
                "prompt": f"""
Create an infographic poster:
- Title: "Why Choose TechITFactory?"
- 6 Icons with text:
  1. 100% Practical Projects
  2. Telugu + English
  3. Lifetime Access
  4. Interview Prep
  5. Certificate
  6. WhatsApp Support
- Color scheme: Professional tech colors
- Footer: "Enroll at ₹2,999"
"""
            },
            {
                "type": "Limited Offer",
                "prompt": f"""
Create an urgency poster:
- Big text: "LAST 48 HOURS"
- Course: {course_title}
- Countdown timer graphic
- Original: ₹9,999 (strikethrough)
- Now: ₹2,999
- Red and yellow colors for urgency
- CTA: "Grab Your Seat Now"
"""
            }
        ],
        
        "social_media_reels": {
            "monday_motivation": "Show before/after salary comparison with inspiring music",
            "tutorial_tuesday": "Quick 30-second tip from the course",
            "transformation_wednesday": "Student success story with testimonial",
            "throwback_thursday": "Common mistakes beginners make (relatable content)",
            "feature_friday": "Showcase a cool project from the course",
            "student_spotlight_saturday": "Interview with successful student",
            "sunday_prep": "Week ahead preview and motivational message"
        }
    }
