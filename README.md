Note: Python version used 3.12.7, Django version used 5.1.3

Set-up details:
1. Create a virtaul environemnt using venv, to isolate the project setup from global setup.
2. activate the virtual environemnt. For macOS use the command "source myenv/bin/activate".
3. Install all the dependencies mentioned in the requirement.txt.
4. Create a db in mysql database server with the name "linkedinMsgGenerator". This is to save the details of the target profile user.
5. Replace the credentials with your credentials for database in settings.py.
6. Insert your openAI key in settings.py.
7. make the migrations to complete database setup.
8. run server using "py manage.py runserver"
9. To set up front-end, access msg_generator_ui folder
10. Install all dependencies using command npm i
11. run server using "npm start" command

APIs:
1. /
   Method: Post
   Description: For scraping the details of the target profile, such as name, location and posts.
   Payload:
   {
    "username": likedin_username,
    "password": linkedin_password,
    "profileUrl":target_url
   }
   response:
   {
    "details": {
        "name": "Kunal Shah",
        "location": "San Francisco, California, United States",
        "posts": [
            "Top 20 India apps by downloads Oct 2024!Position changes are in comparison to September.- The top 2 Meesho and Flipkart continue to hold their spots for 3 straight months now! While Meesho grew their downloads by 1M in Oct, Flipkart actually acquired 5.5M users lesser than Sep but still managed to retain its spot.- Gametion Technologies Pvt. Ltd. (Ludo King) and PhonePe continued holding their spot for 2 months in a row despite 1.1M lesser downloads each.- Zepto is making BIG gains! While it climbed 4 positions last month, this month it climbed 10 positions and made its way into the Top 5 by securing 7M more downloads compared to the previous month! Zepto launched several campaigns in October with over 200 creatives, that too only on Meta! - Jio Cinema, Disney+ Hotstar and Crafto made some significant jumps to enter the Top 20 list. Jio Cinema was a slam dunk entry with the new Big Boss season while Crafto saw a big bump with their October Diwali campaigns!Source: sensortower",
            "UA teams need to get themselves visibility on post install metrics like Retention, Ad rev and IAP rev by relevant cohorts like UA campaigns, Country, App Version and Experiments to see these opportunities!Talk to us at Segwise.ai if you want to enable this in your teams 🤝",
            "Every day marketers spend too much time optimizing marketing costs, where one of the key metrics is [CAC]. While this strategy sounds reasonable, it's actually quite limited. Why? If we segment users by [revenue_30d] we can figure out ...1/ [CAC] variance is much lower than [LTV]. In other words, you can't optimize [CAC] to zero. Min [CAC] per month per segment, on average, is just 20% lower than the Max value. So there is no big room for improvement here.2/ The first 3 segments of users simply can't pay back at all. [LTV] of these segments is so low, that [CAC] optimization here is mostly a waste of time. Increasing the initial price, and focusing on monetization conversions, even if it sounds out of scope, could actually heavily increase the chances of breaking even.hashtag#cac hashtag#ltv hashtag#segmentation",
            "As a gaming PM, do you think subtle game elements like small animations and shadows make a difference to the overall game experience? 🤔Check out the full episode D-Zero by Segwise.ai with Nilay in the comments!",
            "hashtag#MarketMapMondays - Today, let’s dive into the impact of Gen AI on GAMING. Gaming is already bigger than all other forms of entertainment put together - expected to be $321 billion in 2026 vs Music ($36 b), Cinema ($46b) and OTT ($114b).Yet, as Bain highlights, only about 5% of gaming content today is developed with Generative AI. Industry experts predict that within 5-10 years, this number could surge to over 50%, creating an expansive opportunity for founders at the Gen AI x Gaming nexus.Alexandre Dewez (20VC), Camille Ha (Eurazeo), and Marie Brayer/Roméo Walter (Fly Ventures) have published an outstanding piece on this very intersection (link to Substack in comments).Broadly the Gen AI opportunity in gaming can be broken down into three core areas:1) Gaming ExperiencesThere’s immense potential for AI-native challenger studios to disrupt and potentially outshine today’s gaming giants (e.g. Gepetto, Realspawn Studios Unleashed Games). The key will be an intensive focus on AI talent, a gap many established studios are still racing to fill.2) Asset GenerationGenerative AI is transforming asset creation, led currently by broad players like Midjourney, Stability AI, and Eleven Labs. While these generalists lead, we anticipate the emergence of gaming-specific asset generators that dive even deeper into this space.(e.g. Leonardo.Ai, Kaedim, Kinetix, Spectral Labs, Cascadeur, Copresence)3) Gaming InfrastructureHistorically challenging for startups due to gaming’s project-based nature, infrastructure presents intriguing possibilities for AI-native platforms. While ad platforms (Unity, Meta, Google), gaming stores (Steam, Epic Games), and game engines (Unreal, Unity, Roblox) have set the pace, an AI-native game engine could be poised to challenge the likes of Unreal and Unity.India is emerging as the world’s largest gaming market, with 568 million gamers and record setting 9.5 billion game app downloads in 2023 alone. However, monetization still lags behind this scale—the market reached $2.2 billion in 2023 but is projected to grow to $8.6 billion by 2028.We believe, for Indian founders, the significant opportunity likely lies in asset generation and gaming infrastructure, not in the studios themselves. At Antler India, we recently invested in Segwise.ai (Brijesh Bharadwaj and Shobhit Gupta), reimagining User Acquisition with AI-native agents.If you’re building AI-driven challengers within gaming infrastructure, let’s connect.with Ojasvi Srivastava Neha Reddy Nitin Sharma Rajiv Srivatsahashtag#GamingIndustry hashtag#GenerativeAI hashtag#AIXGaming hashtag#GamingTech hashtag#GameDevelopment hashtag#StartupOpportunity hashtag#IndianGaming hashtag#VentureCapital hashtag#AntlerIndia hashtag#DigitalTransformation hashtag#AIFounders hashtag#GameDesign hashtag#TechTrends"
        ]
    }
   }

2. /generate?name={target_user_name}
   Method:Get
   Description: This api takes target_user_name fetches the details from database and uses openAI to create a personalised message
   payload: request params
   response:
   [
    "Hi Kunal, I’m impressed by your insights on user acquisition and the transformative impact of Gen AI in gaming. I’d love to connect and explore potential synergies in this exciting space."
]
