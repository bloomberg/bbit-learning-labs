// components/Navbar.js
import Link from 'next/link';
import { useState } from 'react';

export default function Navbar() {
    return (
        <nav>
            <div className="nav-div">
                <Link href={'/'}>
                    <span id="navbar-home-span-wrapper">
                        <span id="navbar-home-span">The Tech Lab Times</span>
                    </span>
                </Link>
                <div className="navbar-navigation-wrapper" id="navbar-default">
                    <div className="navbar-list-wrapper">
                        <ul className="navbar-list">
                            <li>
                                <Link href='/news'><span className="menu-item" aria-current="page">News</span></Link>
                            </li>
                            <li>
                                <Link href='/stocks'><span className="menu-item">Stocks</span></Link>
                            </li>
                            <li>
                                <p id='nav-divider'>|</p>
                            </li>
                            <li>
                                <Link href='https://github.com/bloomberg/bbit-learning-labs' target="_blank"><span className="menu-item">Github</span></Link>
                            </li>
                            <li>
                                <Link href='/'><span className="menu-item">Documentation</span></Link>
                            </li>
                            <li>
                                <Link href='/'><span className="menu-item">Redis</span></Link>
                            </li>
                            <li>
                                <Link href='/'><span className="menu-item">Stretch Goals</span></Link>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </nav>
    );
}
