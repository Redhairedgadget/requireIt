import os
import traceback
import sys

sys.path.append("C:/Users/igorc/PycharmProjects/requireIt/backend")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'requireIt.settings')


def add_industry(industry):
    i = Industry.objects.create(industry=industry)
    return i

def add_requirement(requirement, obligatory, answer=None):
    r = Requirement.objects.create(requirement=requirement, obligatory=obligatory, answer=answer)
    return r

def add_webapp(title):
    w = WebApp.objects.create(title=title)
    return w

def populate():
    # All the industries
    add_industry(industry="Business")
    add_industry(industry="Entertainment")
    add_industry(industry="Education")
    add_industry(industry="Media")
    add_industry(industry="NGO")

# All requirements
    #Industy reqs

        # Brochure
    add_requirement('Gallery/showcase', True,)
    add_requirement('Customer reviews/testimonials', True)
    add_requirement('Blog section (optional: categories, tags)', True)
    add_requirement('Lead generation elements ("Only ... days left" bar, "Subscribe and get bonuses" pop-up, etc.)',
                    True)
    add_requirement('Team (as a separate page or section)', True)
    add_requirement('FAQ', True)
    add_requirement('Date of the event (in case of event)', True)
    add_requirement('Information/design complexity balance', False)

        # E-commerce
    add_requirement('Basket and Gallery', True)
    add_requirement('User-generated reviews/ratings/comments for the item', True)
    # add_requirement('Online payments', True)
    add_requirement('Special offers', True)
    add_requirement('Wish list', True)
    add_requirement('Related items', True)
    #add_requirements('FAQ') -> brochure
    add_requirement('Customizable user dashboard with user statistics', True)
    add_requirement('Find-in-store', True)
    add_requirement('Search with autofill', True)
    add_requirement('User registration, login/logout', True)
    add_requirement('Additional security measures (firewall, privacy policy link)', True)
    add_requirement('"Item available" notification', True)
    add_requirement('Shipping information', True)
    add_requirement('Return policy', True)
    #add_requirement('Lead generation elements') -> brochure
    add_requirement('Customer support', True)

        # Blog
    #add_requirement('Blog section') -> Brochure
    add_requirement('Visitors-generated ratings/likes-dislikes', True)
    add_requirement('Commentary section', True)

        # Lead Generation
    add_requirement('Call-action sections, elements and buttons', True)
    add_requirement('Short information sections ("why choose us", numbers, statistics, etc.)', True)
    #add_requirement('Testimonials') -> brochure
    #add_requirement('Team') -> brochure
    add_requirement('Huge date section/countdown (if created for event or as landing page', True)
    # add_requirement('blog') -> brochure
    add_requirement('Focus on appealing design, which makes user stay longer. Lightweight information.', False)
    add_requirement('Transitions and animations to make website look more lively', False)

        # Forum
    # add_requirement('FAQ') -> brochure
    add_requirement('Conditions of usage', True)
    add_requirement('Censoring automation', True)
    # add_requirement('User registration') -> e-commerce
    # add_requirement('Customizable user dashboard (with or without user statistics)', True) -> ecommerce
    add_requirement('Private messaging', True)
    add_requirement("Users' reputation system", True)
    add_requirement('Post categories and subcategories with tags', True)
    add_requirement('Post creation by users', True)
    # add_requirement('Search with autofill') -> ecommerce
    add_requirement('Choosing among searches which are supporting not only autofill, but also smart search', False)

        # Online newspaper
    add_requirement('Categories of articles with tags', True)
    add_requirement('Front page with latest articles', True)
    # add_requirement('Commentary section') --> Blog
    # "likes/dislikes" -> blog
    # add_requirement('registration') -> e-commerce

        # Streaming
    # add_requirement('likes/dislikes') -> blog
    add_requirement('Content library with categories', True)
    # add_requirement('search') -> ecommerce
    # add_requirement('user registration') -> ecommerce
    # add_requirement('customizable dashboard') -> e-commerce
    add_requirement('User upload support (with or without upload automation)', True)
    add_requirement('Content share and embed', True)
    add_requirement('Playlists', True)
    add_requirement('Subscription to author of content', True)
    add_requirement('Creative studio for authors', True)
    add_requirement('Report function', True)
    add_requirement('Auto-moderation', True)
    add_requirement("Licencing author's content", True)
    add_requirement('Terms of use', True)
    add_requirement('Financial liability', True)
    add_requirement('Monetization system', True)
    add_requirement('Pay-per-view', True)
    add_requirement('Content delivery network', True)
    add_requirement('Token-based security', True)
    add_requirement('Domain restriction', True)
    add_requirement('Watermark', True)
    # add_requirement('FAQ') -> brochure
    # add_requirement('Customer support') -> ecommerce

        # Study portal
    # add_requirement('Rgistration') -> ecommerce
    add_requirement('Registration for lessons/classes/events', True)
    add_requirement('Grade system', True)
    add_requirement('Studying milestones', True)
    add_requirement('Access to study material', True)
    add_requirement('Tests', True)
    # add_requirement('FAQ') -> brochure
    # add_requirement('Customer support') -> ecommerce

        # Online game
    add_requirement('Game software (visual design, gameplay, music)', True)
    add_requirement('Sign-up bonuses', True)
    add_requirement('Frequent player bonuses', True)
    # add_requirement('registration') -> ecommerce
    # add_requirement('dashboard') -> ecommerce
    add_requirement('Tutorials', True)
    add_requirement('Chats (group and private)', True)
    add_requirement('Video/call streams (group and private)', True)
    add_requirement("Gamers' portal", True)
    # add_requirement('FAQ') -> brochure
    # add_requirement('Customer support') -> ecommerce
    add_requirement('Promotions for seasonal events', True)
    add_requirement('Big memory storage available', False)
    add_requirement('Lightweight visuals', False)
    add_requirement('Either buy a premade gaming software from some provider or hire a team/agency which specializes in gaming development', False)

        # Gambling
    add_requirement('Gambling management system', True)
    add_requirement('Coverage of betting markets', True)
    add_requirement('Access to a selection of games', True)
    add_requirement('Gambling licence', True)
    # add_requirement('customer support') -> ecommerce
    add_requirement('Live casino module (live video streaming, chats, etc.)', True)
    add_requirement('In-play bettings, pre-play bettings', True)
    # add_requirement('registration') -> ecommerce
    add_requirement('VIP loyalty program', True)
    add_requirement('Bonuses system (sign-up bonuses, deposit bonuses, free bits)', True)
    # add_requirement('dashboard') -> ecommerce
    add_requirement('Tournaments', True)
    add_requirement('In-game statistics (players, round etc.)', True)
    # add_requirement('Promotions for seasonal events', True) -> online game
    add_requirement('Betting assistance and tutorials', True)
    add_requirement('Fraud detection', True)
    # add_requirement('Find an igaming software provider', False) -> online game
    # add_requirement('Lightweight visuals', False) -> online game
    # add_requirement('Big memory storage available', False) -> online game

    # Question reqs

        # Industry?

            # Business
    add_requirement('Call-to-action elements related to selling', True, 'Business')
    add_requirement('Appropriate loading speed', False, 'Business')
    # add_requirement('Big memory storage available', False) -> online game

            # Media
    add_requirement('Focus on good readability of shown information (big enough fonts, eye-health-friendly colors)',
                    False, 'Media')
    add_requirement('Clear design, some lead generation elements are ok, but not necessary', False, 'Media')

            # Entertainement
    # add_requirement('Appropriate loading speed', False) -> business
    add_requirement('Design as appealing as possible', False, 'Entertainment')

            # Education
    add_requirement('Lightweight intuitive design, focus on information accessibility', False, 'Education')
    add_requirement('Call-to actions encouraging to continue learning', False, 'Education')

            # NGO
    add_requirement('Focus on Lead Generation, SEO and Social Media integration in design', False, 'NGO')

        # Revenue model?

            # Ads
    add_requirement('Ads integration', True, 'Advertisement')

            # One-time payments
    add_requirement('Online payments support', True, 'One-time payments')
    add_requirement('Bookings, possibly with availability counter of interactive calendar', True, 'One-time payments')

            # Subscriptions
    add_requirement('Subscription plans', True, 'Subscription plans')
    add_requirement('Automatic charging', True, 'Subscription plans')
    add_requirement("Automatic blocking of service in case if user doesn't renew the plan", True, 'Subscription plans')

            # Business specific
    add_requirement('Price list', True, 'bspecial')

        # Local/global

            # Local
    add_requirement('Online payment system with locally popular systems (e.g kiwi in Russia, eximbay in Korea)', True, 'Local')

            # Global
    add_requirement('Online payments with internationally popular systems (e.g. Paypal)', True, 'Global')
    add_requirement('Multi-currency support', True, 'Global')

        # Target audience?

            # Children/teenagers
    add_requirement('Colorful design appealing to children/kids', False, 'Children, teenagers')
    add_requirement('More of call-to-action elements', False, 'Children, teenagers')
    add_requirement('Speed of action, instant gratification', False, 'Children, teenagers')

            # Young adults without children
    add_requirement('Design appealing to young adults without children', False, 'Young adults without children')

            # Families
    add_requirement('Family-oriented design', False, 'Families')

            # Elderly
    add_requirement('Make design as intuitive and clean as possible', False, 'Elderly')
    add_requirement('Bigger fonts and buttons', False, 'Elderly')

        # Scope?

            # Community/niche
    add_requirement('Using community specific memes', False, 'Community/Niche')
    add_requirement("Create content with community's terminology in mind", False, 'Community/Niche')

            # Generation
    add_requirement('References in design/content to culture elements, belonging to chosen generation', False, 'Generation')
    add_requirement('Avoid creating topics/elements, which may be offencive for generation', False, 'Generation')
    add_requirement('Try to inflict nostalgic feelings with design/content', False, 'Generation')

            # Everyone
    add_requirement('Make sure that content is not offensive to any social group', False, 'Everyone')

    # General
    add_requirement('Contact us page', True, 'general')
    add_requirement('About page', True, 'general')
    add_requirement('Domain', True, 'general')
    add_requirement('Server/hosting', True, 'general')
    add_requirement('SSL certificate', True, 'general')
    add_requirement('Newsletter', True, 'general')
    add_requirement('Social media integration', True, 'general')
    add_requirement('Maintenance', True, 'general')
    add_requirement('Custom logo', True, 'general')
    add_requirement('Cusotm design', True, 'general')
    add_requirement('SEO', True, 'general')
    add_requirement('Loading time', True, 'general')


    # Webapps

    # def all_inds():
    #     result = []
    #     all = Industry.objects.all()
    #     for industry in all:
    #         result.append(industry)
    #     return result

        # Brochure

    brochure_reqs = [
                    Requirement.objects.get(requirement='Gallery/showcase'),
                    Requirement.objects.get(requirement='Customer reviews/testimonials'),
                    Requirement.objects.get(requirement='Blog section (optional: categories, tags)'),
                    Requirement.objects.get(requirement='Lead generation elements ("Only ... days left" bar, "Subscribe and get bonuses" pop-up, etc.)'),
                    Requirement.objects.get(requirement='Team (as a separate page or section)'),
                    Requirement.objects.get(requirement='FAQ'),
                    Requirement.objects.get(requirement='Date of the event (in case of event)'),
                    Requirement.objects.get(requirement='Information/design complexity balance')
                     ]


    brochure_instance = add_webapp(title='Brochure')
    brochure_instance.requirements.set(brochure_reqs)
    brochure_instance.industries.add(*Industry.objects.all())


        # E-commerce

    ecommerce_reqs = [
                    Requirement.objects.get(requirement='Basket and Gallery'),
                    Requirement.objects.get(requirement='User-generated reviews/ratings/comments for the item'),
                    Requirement.objects.get(requirement='Special offers'),
                    Requirement.objects.get(requirement='Wish list'),
                    Requirement.objects.get(requirement='Related items'),
                    Requirement.objects.get(requirement='FAQ'),
                    Requirement.objects.get(requirement='Customizable user dashboard with user statistics'),
                    Requirement.objects.get(requirement='Find-in-store'),
                    Requirement.objects.get(requirement='Search with autofill'),
                    Requirement.objects.get(requirement='User registration, login/logout'),
                    Requirement.objects.get(requirement='Additional security measures (firewall, privacy policy link)'),
                    Requirement.objects.get(requirement='"Item available" notification'),
                    Requirement.objects.get(requirement='Shipping information'),
                    Requirement.objects.get(requirement='Return policy'),
                    Requirement.objects.get(requirement='Lead generation elements ("Only ... days left" bar, "Subscribe and get bonuses" pop-up, etc.)'),
                    Requirement.objects.get(requirement='Customer support'),
                    ]

    ecommerce_instance = add_webapp(title='E-commerce')
    ecommerce_instance.requirements.set(ecommerce_reqs)
    ecommerce_instance.industries.add(Industry.objects.get(industry="Business"))

        # Blog

    blog_reqs = [
                Requirement.objects.get(requirement='Blog section (optional: categories, tags)'),
                Requirement.objects.get(requirement='Visitors-generated ratings/likes-dislikes'),
                Requirement.objects.get(requirement='Commentary section'),
                ]

    blog_instance = add_webapp(title='Blog')
    blog_instance.requirements.set(blog_reqs)
    blog_instance.industries.set([Industry.objects.get(industry='Media'), Industry.objects.get(industry='Entertainment')])

        # Lead generation website

    leadgen_reqs = [
                    Requirement.objects.get(requirement='Call-action sections, elements and buttons'),
                    Requirement.objects.get(requirement='Short information sections ("why choose us", numbers, statistics, etc.)'),
                    Requirement.objects.get(requirement='Customer reviews/testimonials'),
                    Requirement.objects.get(requirement='Team (as a separate page or section)'),
                    Requirement.objects.get(requirement='Huge date section/countdown (if created for event or as landing page)'),
                    Requirement.objects.get(requirement='Blog section (optional: categories, tags)'),
                    Requirement.objects.get(requirement='Focus on appealing design, which makes user stay longer. Lightweight information.'),
                    Requirement.objects.get(requirement='Transitions and animations to make website look more lively'),
                    ]

    leadgen_instance = add_webapp(title='Lead generation website (e.g. landing page)')
    leadgen_instance.requirements.set(leadgen_reqs)
    leadgen_instance.industries.add(*Industry.objects.all())

        # Forum

    forum_reqs = [
                  Requirement.objects.get(requirement='FAQ'),
                  Requirement.objects.get(requirement='Conditions of usage'),
                  Requirement.objects.get(requirement='Censoring automation'),
                  Requirement.objects.get(requirement='User-generated reviews/ratings/comments for the item'),
                  Requirement.objects.get(requirement='Customizable user dashboard with user statistics'),
                  Requirement.objects.get(requirement='Private messaging'),
                  Requirement.objects.get(requirement="Users' reputation system"),
                  Requirement.objects.get(requirement='Post categories and subcategories with tags'),
                  Requirement.objects.get(requirement='Post creation by users'),
                  Requirement.objects.get(requirement='Search with autofill'),
                  Requirement.objects.get(requirement='Choosing among searches which are supporting not only autofill, but also smart search'),
                 ]

    forum_instance = add_webapp(title='Forum')
    forum_instance.requirements.set(forum_reqs)
    forum_instance.industries.set([Industry.objects.get(industry='Media'), Industry.objects.get(industry='Education')])

        # Online newspaper

    newspaper_reqs = [
                Requirement.objects.get(requirement='Categories of articles with tags'),
                Requirement.objects.get(requirement='Front page with latest articles'),
                Requirement.objects.get(requirement='Commentary section'),
                Requirement.objects.get(requirement='Visitors-generated ratings/likes-dislikes'),
                Requirement.objects.get(requirement='User registration, login/logout'),
                ]

    newspaper_instance = add_webapp(title='Online newspaper')
    newspaper_instance.requirements.set(newspaper_reqs)
    newspaper_instance.industries.add(Industry.objects.get(industry='Media'))

        # Streaming

    streaming_reqs = [
                Requirement.objects.get(requirement='Visitors-generated ratings/likes-dislikes'),
                Requirement.objects.get(requirement='Content library with categories'),
                Requirement.objects.get(requirement='Search with autofill'),
                Requirement.objects.get(requirement='User registration, login/logout'),
                Requirement.objects.get(requirement='Customizable user dashboard with user statistics'),
                Requirement.objects.get(requirement='User upload support (with or without upload automation)'),
                Requirement.objects.get(requirement='Content share and embed'),
                Requirement.objects.get(requirement='Playlists'),
                Requirement.objects.get(requirement='Subscription to author of content'),
                Requirement.objects.get(requirement='Creative studio for authors'),
                Requirement.objects.get(requirement='Report function'),
                Requirement.objects.get(requirement='Auto-moderation'),
                Requirement.objects.get(requirement="Licencing author's content"),
                Requirement.objects.get(requirement='Terms of use'),
                Requirement.objects.get(requirement='Financial liability'),
                Requirement.objects.get(requirement='Monetization system'),
                Requirement.objects.get(requirement='Pay-per-view'),
                Requirement.objects.get(requirement='Content delivery network'),
                Requirement.objects.get(requirement='Token-based security'),
                Requirement.objects.get(requirement='Domain restriction'),
                Requirement.objects.get(requirement='Watermark'),
                Requirement.objects.get(requirement='FAQ'),
                Requirement.objects.get(requirement='Customer support'),
                ]

    streaming_instance = add_webapp(title='Streaming website')
    streaming_instance.requirements.set(streaming_reqs)
    streaming_instance.industries.set([Industry.objects.get(industry='Media'), Industry.objects.get(industry='Entertainment'), Industry.objects.get(industry='Education')])

        # Study portal

    portal_req = [
                Requirement.objects.get(requirement='User registration, login/logout'),
                Requirement.objects.get(requirement='Registration for lessons/classes/events'),
                Requirement.objects.get(requirement='Grade system'),
                Requirement.objects.get(requirement='Studying milestones'),
                Requirement.objects.get(requirement='Access to study material'),
                Requirement.objects.get(requirement='Tests'),
                Requirement.objects.get(requirement='FAQ'),
                Requirement.objects.get(requirement='Customer support'),
                ]

    portal_instance = add_webapp(title='Study portal')
    portal_instance.requirements.set(portal_req)
    portal_instance.industries.add(Industry.objects.get(industry='Education'))

        # Online game

    game_req = [
                Requirement.objects.get(requirement='Game software (visual design, gameplay, music)'),
                Requirement.objects.get(requirement='Sign-up bonuses'),
                Requirement.objects.get(requirement='Frequent player bonuses'),
                Requirement.objects.get(requirement='User registration, login/logout'),
                Requirement.objects.get(requirement='Customizable user dashboard with user statistics'),
                Requirement.objects.get(requirement='Tutorials'),
                Requirement.objects.get(requirement='Chats (group and private)'),
                Requirement.objects.get(requirement='Video/call streams (group and private)'),
                Requirement.objects.get(requirement="Gamers' portal"),
                Requirement.objects.get(requirement='FAQ'),
                Requirement.objects.get(requirement='Customer support'),
                Requirement.objects.get(requirement='Promotions for seasonal events'),
                Requirement.objects.get(requirement='Big memory storage available'),
                Requirement.objects.get(requirement='Lightweight visuals'),
                Requirement.objects.get(requirement='Either buy a premade gaming software from some provider or hire a team/agency which specializes in gaming development'),
                ]

    online_game_instance = add_webapp(title='Online game')
    online_game_instance.requirements.set(game_req)
    online_game_instance.industries.set([Industry.objects.get(industry="Entertainment"), Industry.objects.get(industry='Education')])

        # Gambling

    gambling_req = [
                Requirement.objects.get(requirement='Gambling management system'),
                Requirement.objects.get(requirement='Coverage of betting markets'),
                Requirement.objects.get(requirement='Access to a selection of games'),
                Requirement.objects.get(requirement='Gambling licence'),
                Requirement.objects.get(requirement='Customer support'),
                Requirement.objects.get(requirement='Live casino module (live video streaming, chats, etc.)'),
                Requirement.objects.get(requirement='In-play bettings, pre-play bettings'),
                Requirement.objects.get(requirement='User registration, login/logout'),
                Requirement.objects.get(requirement='VIP loyalty program'),
                Requirement.objects.get(requirement='Bonuses system (sign-up bonuses, deposit bonuses, free bits)'),
                Requirement.objects.get(requirement='Customizable user dashboard with user statistics'),
                Requirement.objects.get(requirement='Tournaments'),
                Requirement.objects.get(requirement='In-game statistics (players, round etc.)'),
                Requirement.objects.get(requirement='Promotions for seasonal events'),
                Requirement.objects.get(requirement='Fraud detection'),
                Requirement.objects.get(requirement='Either buy a premade gaming software from some provider or hire a team/agency which specializes in gaming development'),
                Requirement.objects.get(requirement='Lightweight visuals'),
                Requirement.objects.get(requirement='Big memory storage available'),
                ]

    gambling_instance = add_webapp(title='Gambling website')
    gambling_instance.requirements.set(gambling_req)
    gambling_instance.industries.add(Industry.objects.get(industry='Entertainment'))

def main():
    populate()

# Start execution here!
if __name__ == '__main__':


    import django
    django.setup()

    from questionTree.models import Industry, Requirement, WebApp

    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt as e:
        raise e
    except SystemExit as e:
        raise e
    except Exception as e:
        print('ERROR: Unexpected exception')
        print(str(e))
        traceback.print_exc()
        os._exit(1)