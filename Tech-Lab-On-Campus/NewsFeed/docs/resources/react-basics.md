# React Basics

React is a popular JavaScript library for building user interfaces. Developed by Facebook, it allows developers to create reusable UI components and manage application state efficiently.

## Key Features
1. **Component-Based Architecture**: Build reusable, isolated pieces of UI.
2. **Virtual DOM**: Efficiently updates the DOM by calculating differences between updates.
3. **Unidirectional Data Flow**: Simplifies data management by ensuring data flows in one direction.
4. **JSX Syntax**: Combines JavaScript with HTML-like syntax for building UI components.

## Core Concepts

### 1. Components
Components are the building blocks of a React application. They can be:
- **Functional Components (Recommended)**: Defined as JavaScript functions.
- **Class Components**: Defined as ES6 classes.

Example of a Functional Component:
```jsx
function Greeting() {
  return <h1>Hello, React!</h1>;
}

export default Greeting;
```

### 2. JSX

JSX (JavaScript XML) allows you to write HTML-like syntax in JavaScript. It is typically the return of the functional
component.

Example:
```jsx

function foo(): JSX.Element { // The return type for custom React components is typically JSX
  const element = <h1>Welcome to React!</h1>;
  return element;
}
```

It is possible to inject Javascript/dynamic content into JSX using `{}` as a wrapper.

**NOTE: If/Else statements are not usable in the JSX section, instead use a ternary operator ( bool ? true : false) or**
**use a callback function to render what you need.**

Examples:
```jsx
// Working example
import React from 'react';

export default function Counter(props: { count }) {
  return (
    <div>
      {/* Inlined javascript variable count (and comment) */}
      {props.count > 10 ? <p>Count: {count}</p> : <p>Max count (10) reached!<p/>}
      <button onClick={() => setCount(count + 1)}>Increment</button> {/* Callback function that adds to the count */}
    </div>
  );
}
```

See more at the [react docs](https://react.dev/learn/writing-markup-with-jsx).

### 3. Props

Props (short for properties), are used to pass data from parent to child components. Props are objects that can contain
any data you need to pass down.

Example:
```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

export default Welcome;
```

### 4. State

State is used to manage dynamic data within a component.

Example:
```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

export default Counter;
```

### 5. Component

Components follow a lifecycle to manage behavior at various stages, mainly the mounting, updating, and unmounting phases.

Key stages:
* `componentDidMount`
* `componentDidUpdate`
* `componentWillUnmount`

Example:
```jsx
class App extends React.Component {
  componentDidMount() {
    console.log('Component Mounted');
  }

  render() {
    return <h1>React Lifecycle</h1>;
  }
}
```

This is now managed via functional components and the use of states and hooks, but understanding the lifecycle is helpful
to resolve bad rendering and understanding rendering logic.


## Advantages
* Reusable Components: Break UI into reusable and modular pieces.
* Efficient Rendering: The Virtual DOM minimizes updates to the actual DOM.
* Strong Ecosystem: Includes tools like React Router and state management libraries like Redux.

## Basic Project Structure
* `src`: Contains application code.
* `public`: Static assets like images or HTML.

## Example Application

```jsx
import React from 'react';

function App() {
  const name = 'React';

  return (
    <div>
      <h1>Welcome to {name}!</h1>
    </div>
  );
}

export default App;
```

Run the application:
```
npm start
```

## Use Cases
1. Single Page Applications (SPAs): Build interactive and dynamic web apps.
2. Reusable Components: Shareable components for UI consistency.
3. Interactive UIs: Handle user input and update views in real-time.
4. Mobile Development: Extend with React Native for mobile apps.


## Additional Resources
1. [React docs](https://react.dev/learn)
2. [Writing HTML with JSX](https://react.dev/learn/writing-markup-with-jsx)
3. [React hooks](https://react.dev/reference/react/hooks)
