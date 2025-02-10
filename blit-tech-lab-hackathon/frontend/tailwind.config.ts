import type { Config } from "tailwindcss";

export default {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: '#ffffff',
        secondaryBackground: '#EDF2FA',
        foreground: '#000000',
        title: '#000000',
        body: '#1C1C1C',
        primary: '#FFA028',
        secondary: '#1C1C1C',
        highlight: '#FFA028',
      },
    },
  },
  plugins: [],
} satisfies Config;
