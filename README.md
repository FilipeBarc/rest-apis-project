# REST APIs Recording Project

API Description: Store Management and User Authentication API

Overview:
The Store Management and User Authentication API is a robust and secure solution that enables users to perform various actions such as user login, creating stores, adding items and tags, managing users, and implementing different authorization layers. The API is designed to store data in a relational database, ensuring data integrity and seamless scalability. Additionally, the API incorporates an admin account with elevated privileges for managing system-wide settings and permissions.

Authentication:
The API employs JWT (JSON Web Tokens) for user authentication, ensuring a secure and stateless authentication process. Users can register an account and subsequently log in, receiving a unique JWT upon successful authentication. The JWT will be used for subsequent requests to authorize actions based on the user's role and permissions.

User Management:

Register User: Allows users to create new accounts with unique credentials, ensuring secure user access.
User Login: Enables users to log in and receive a JWT for authorization in subsequent requests.
User Roles: Supports multiple user roles (e.g., regular user, store owner, admin), each with specific permissions.
Store Management:

Create Store: Authenticated users with the "store owner" role can create new stores with relevant details like name, description, and location.
Update Store: Store owners can update their stores' information, such as description or location.
Delete Store: Allows store owners to delete their own stores, ensuring data privacy and control.
View Store: Provides a detailed view of a store, including its items and tags.
Item Management:

Add Item: Store owners can add new items to their respective stores, specifying item name, description, and price.
Update Item: Enables store owners to update item details like price or description.
Delete Item: Store owners can remove items from their stores, maintaining data accuracy.
View Item: Provides a comprehensive view of an item, including its tags and related information.
Tag Management:

Add Tag: Allows store owners to add descriptive tags to their items for better categorization and searchability.
Update Tag: Enables store owners to update tag names or descriptions.
Delete Tag: Store owners can remove tags associated with their items, keeping data relevant.
View Tag: Provides information about a specific tag, including associated items.
Authorization Layers:
The API implements different authorization layers based on user roles. Each API endpoint is secured, allowing access only to users with the appropriate role and permissions. For instance, only store owners can modify or delete their stores, while regular users can view store and item details.

Admin Account:
An admin account is included in the system, holding elevated privileges for managing users, stores, items, and tags. The admin can grant or revoke permissions, view system logs, and perform administrative tasks to ensure smooth operation and security.

Database:
The API uses a relational database to store user account details, store information, item data, tag details, and authorization configurations securely.

Overall, the Store Management and User Authentication API offers a powerful and flexible solution for managing stores and users while maintaining robust security and privacy controls. It enables businesses to seamlessly integrate their applications with the API to streamline store operations and ensure a smooth user experience.