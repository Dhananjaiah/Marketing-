#!/usr/bin/env python3
"""
Simple runner script for TechITFactory Marketing Strategist
Usage: python3 run_strategist.py "Course Title"
"""

import sys
import json
from pathlib import Path

# Import all strategy modules
from strategies import content_generator, funnel_strategy, growth_planner

def print_banner():
    """Print welcome banner"""
    print("="*80)
    print("TechITFactory Marketing Strategist")
    print("Specialized for Indian Learners | Telugu Audience | DevOps/Kubernetes/MLOps")
    print("="*80)
    print()

def summarize_goals(course_title):
    """Summarize key marketing goals"""
    return f"""
🎯 KEY MARKETING GOALS FOR: {course_title}

1. ✅ Create high-converting landing page content
2. ✅ Generate bilingual ad scripts (Telugu + English)
3. ✅ Optimize for SEO and discoverability
4. ✅ Build complete sales funnel (Free → Paid)
5. ✅ Automate outreach (WhatsApp, Telegram, Email)
6. ✅ Design engaging social media content
7. ✅ Establish 30-day growth strategy

Target: Indian learners focusing on practical, hands-on DevOps/MLOps skills
Focus: Trust, FOMO, Social Proof, Clear Outcomes
"""

def main():
    """Main execution function"""
    print_banner()
    
    # Get course title
    if len(sys.argv) > 1:
        course_title = " ".join(sys.argv[1:])
    else:
        course_title = "Complete DevOps with Kubernetes"
        print(f"No course title provided. Using default: {course_title}")
        print()
    
    print(summarize_goals(course_title))
    
    # Generate all marketing materials
    print("\n📝 Generating marketing materials...\n")
    
    strategy = {
        "course_title": course_title,
        "landing_page": content_generator.generate_landing_page(course_title),
        "ad_scripts": content_generator.generate_ad_scripts(course_title),
        "seo_content": content_generator.generate_seo_content(course_title),
        "sales_copy": content_generator.generate_sales_copy(course_title),
        "email_sequence": content_generator.generate_email_sequence(course_title),
        "automation_messages": content_generator.generate_automation_messages(course_title),
        "visual_content": content_generator.generate_visual_content(course_title),
        "funnel_strategy": funnel_strategy.generate_funnel(course_title),
        "pricing_model": funnel_strategy.generate_pricing(course_title),
        "conversion_boosters": funnel_strategy.generate_conversion_boosters(),
        "growth_plan": growth_planner.generate_30_day_plan(course_title),
        "content_calendar": growth_planner.generate_content_calendar(course_title),
        "influencer_outreach": growth_planner.generate_influencer_strategy(course_title),
        "community_strategy": growth_planner.generate_community_strategy(course_title)
    }
    
    # Save to JSON file
    # Sanitize filename to prevent directory traversal and filesystem issues
    import re
    safe_filename = re.sub(r'[^a-z0-9_\-]', '_', course_title.lower())
    safe_filename = re.sub(r'_+', '_', safe_filename).strip('_')
    output_file = f"marketing_strategy_{safe_filename}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(strategy, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Complete marketing strategy generated!")
    print(f"📁 Saved to: {output_file}\n")
    
    # Print immediate action items
    print("="*80)
    print("🚨 IMMEDIATE ACTION ITEMS (MUST FIX FOR HIGHER CONVERSIONS):")
    print("="*80)
    print("1. 🔥 Add countdown timer to landing page (creates urgency)")
    print("2. 🔥 Make CTA button 2x bigger and orange color")
    print("3. 🔥 Add 3 video testimonials above the fold")
    print("4. 🔥 Set up email automation sequence (7-day nurture)")
    print("5. 🔥 Install Facebook pixel for retargeting")
    print("6. 🔥 Create exit-intent popup with 10% discount")
    print("7. 🔥 Add live chat widget for instant support")
    print("8. 🔥 Optimize page loading speed (compress images)")
    print("9. 🔥 Start running Instagram + YouTube ads today")
    print("10. 🔥 Partner with 3 micro-influencers this week")
    print("="*80)
    print("\n💡 Pro Tip: Focus on items 1-3 first for quickest wins!\n")

if __name__ == "__main__":
    main()
