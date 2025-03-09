# Django Blog Application
A simple and functional blog application built with Django, leveraging Class-Based Views (CBV) for the backend. The frontend is designed with Bootstrap, HTML, and JavaScript, ensuring a responsive and dynamic user experience. This project covers key Django concepts, including CRUD operations, user authentication, and templating.

# Tech Horizons
Tech Horizons is a Django-powered blog website where technology enthusiasts and professionals share the latest trends, insights, and innovations. The platform supports user registration, profile management, post creation, and commenting. It also supports a two-step content approval process for blog posts, a search mechanism, and categorized posts.

## Features

- User Registration & Authentication: You can sign up or log in using either a username or an email address. Custom authentication in the project supports both options.
- Profile Management: Every user has a profile with a profile picture, bio, location, and social media links. A logged-in user can edit their account details and profile information.
- Writer Role: Users can become writers (blog authors) after being approved by an administrator. Writers can create, update, or delete posts using dedicated views.
   - Becoming a Writer: Users are not writers by default. An administrator must mark a user’s profile as a writer (by setting the is_writer flag in the Django admin).
   - Post Creation: Once approved as a writer, users can create, update, or delete posts. Posts are created through a dedicated “Add Post” interface that supports rich text (via CKEditor) and image uploads. Newly created or updated posts default to a “Pending” status until reviewed by an administrator.
   - **Post Approval Workflow: When a writer submits a post, its status is set to “Pending.” An administrator must then review and approve the post by changing its status to “Published” so that it is visible on the website.
   - **Categories & Search: Default Category:
   - The system automatically adds an "Uncategorized" category during migrations. When a post is created without a specified category, it will default to “Uncategorized.”
   - Category Navigation: All pages include a list of categories in the navbar. Users can click a category to view all posts belonging to that category.
   - Search: A search form is available on every page via context processors. Users may search posts by title, content, and category.
**Popular Posts & Likes:
   - Popular Posts: The homepage displays popular posts. Popularity is determined by the number of likes a post has received. Posts are annotated with a like count and sorted in descending order of likes.
   - Likes: Authenticated users can like or unlike a post. The like count is updated in real-time, and the count appears on the post detail page.
**Comments: Authenticated users can post comments on published posts. Comments are displayed on the post detail page and sorted by the most recent.
**Draft/Pending/Published: Posts have a status field with three states: Draft, Pending, and Published.
**Post Approval: When a writer submits a post, its status is set to “Pending.” An administrator reviews pending posts and approves them by changing the status to “Published.”
**Adding Posts: Once approved to be a writer, a user can add new posts using the “Create Post” interface. Posts support rich text formatting through a CKEditor integration.
- **Categories & Search: Posts are organized into categories. All pages include a search form (fed through a context processor) and the list of categories appears in the navbar so that users can browse posts by category.
- **Likes & Comments: Readers can like posts. Authenticated users can comment on posts. Like counts and comments are shown on the post detail page.

## How it Works
## Becoming a Writer

- **User Registration:** Any visitor can sign up for an account. Once registered, the user can create a profile.
- **Admin Approval:** By default, users are not writers. An administrator must mark a user’s profile as a writer by setting the is_writer flag (accessible in the Django admin).
- **Post Creation:** Once approved (i.e., is_writer is set to True), a writer can access the “Add Post” page. Writers fill out the post form—which includes fields for title, content (using CKEditor), a snippet, an image, and optionally a new category—and then submit the post.

## Post Approval Process

- **Submission:** When a writer adds or updates a post, the post status is set to “Pending.” This indicates that the post awaits administrative review.
- **Review:** An administrator reviews posts in the Django admin panel. The admin may then change the status to “Published” to make the post publicly viewable.

### Admin Workflow

- **Managing Users:** The administrator can view all registered users in the Django admin. To grant a user writer privileges, the admin should update the user’s associated profile by setting 
- **Approving Posts:** Review all submitted posts with a status of “Pending” in the admin panel. After verifying the content, the admin approves the post by setting its status to “Published.”

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PhantomX95/django-simple-blog.git
   cd django-blog
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the database migrations:

   ```bash
   python manage.py migrate
   ```
  - The migration automatically creates the "Uncategorized" category if it does not exist.

5. The super user is username:admin password:admin, Or create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and visit the application:

   [http://127.0.0.1:8000/]

## Usage

- Access the blog on the homepage and view all posts.
- Users can register, log in, and manage their profiles.
- Admin users can manage blog posts through the Django admin interface.


---

This README provides a comprehensive guide to set up the Django Blog application, explains the core features and technologies, and offers instructions on how to contribute.
