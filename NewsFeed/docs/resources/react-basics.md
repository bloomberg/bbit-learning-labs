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
- **Functional Components**: Defined as JavaScript functions.
- **Class Components**: Defined as ES6 classes.

Example of a Functional Component:
```jsx
function Greeting() {
  return <h1>Hello, React!</h1>;
}

export default Greeting;
```

### 2. JSX

JSX (JavaScript XML) allows you to write HTML-like syntax in JavaScript.

Example:
```jsx
const element = <h1>Welcome to React!</h1>;
```

### 3. Props

Props (short for properties) are used to pass data from parent to child components.

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

### 5. Lifecycle Methods

Class components use lifecycle methods to manage behavior during mounting, updating, and unmounting phases.

Key methods:
* `componentDidMount`
* `componentDidUpdate`
* `componentWillUnmount`

Example:
```
class App extends React.Component {
  componentDidMount() {
    console.log('Component Mounted');
  }

  render() {
    return <h1>React Lifecycle</h1>;
  }
}
```

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

