# Backend Dependency

## Wordpress 
### Rest API - https://developer.wordpress.org/rest-api/
The WordPress REST API provides an interface for applications to interact with your WordPress site by sending and receiving data as JSON (JavaScript Object Notation) objects. The REST API is a developer-oriented feature of WordPress. It provides data access to the content of your site, and implements the same authentication restrictions — content that is public on your site is generally publicly accessible via the REST API, while private content, password-protected content, internal users, custom post types, and metadata is only available with authentication or if you specifically set it to be so.

- Application Base Endpoint - http://localhost/wp-json/techlabs/v1/

#### API Routes, Requests and Responses:
- /get_share_names/
- /buy_share/
- /sell_shares/
- /get_shares/
- /get_share_price/<string:symbol>
- /get_percentage_change/<string:symbol>

#### Dashboard Access
- URL: [http://localhost/wp-admin/](http://localhost/wp-admin/)
- username: `admin`
- password: `password`



