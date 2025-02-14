import Navbar from "@/components/navbar";
import { Html, Head, Main, NextScript } from "next/document";

export default function Document() {
  return (
    <Html lang="en">
      <Head />
      <Navbar/>
      <body className="antialiased">
        <div className="container m-auto">
          <Main />
        </div>
        <NextScript />
      </body>
    </Html>
  );
}
