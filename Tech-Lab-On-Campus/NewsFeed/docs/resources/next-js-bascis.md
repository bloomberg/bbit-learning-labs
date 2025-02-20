
# Next.js Basics

## What is Next.js?

Next.js is a [React](./react-basics.md) framework that enables several extra features, including server-side rendering and generating static websites. It is built on top of Node.js (a server that uses Javascript to run) and can be used to create web applications with React.

## How Next.js Works

Next.js works by allowing developers to create pages in a `pages` directory. Each file in this directory becomes a route in the application, i.e. the file structure is used as the router for pages in the application. Next.js handles the rendering of these pages on the server side, which can improve performance and SEO.

## Benefits of Next.js

- **Server-Side Rendering (SSR):** Improves performance and SEO by rendering pages on the server.
- **Static Site Generation (SSG):** Generates static HTML at build time, which can be served quickly.
- **API Routes:** Allows you to create API endpoints within the same project.
- **Automatic Code Splitting:** Only loads the necessary JavaScript for the page being rendered.
- **Built-in CSS and Sass support:** Easily import CSS and Sass files.
- **Fast Refresh:** Provides instant feedback on edits made to your React components.

## Getting Started with Next.js

To get started with Next.js, follow these steps:

1. **Install Node.js:** Ensure you have Node.js installed on your machine.

2. **Create a new Next.js project:**
    ```bash
    npx create-next-app@latest my-next-app
    cd my-next-app
    ```

3. **Run the development server:**
    ```bash
    npm run dev
    ```

4. **Open your browser:** Navigate to `http://localhost:3000` to see your new Next.js app.

5. **Create a new page:** Add a new file `about.js` in the `pages` directory with the following content:
    ```javascript
    // filepath: NewsFeed/pages/about.js
    export default function About() {
        return <h1>About Page</h1>;
    }
    ```

6. **Visit the new page:** Open `http://localhost:3000/about` in your browser to see the new page.


For more information on how Next works, visit the [official docs](https://nextjs.org/docs/pages/building-your-application).
