import { BrowserRouter as Router,Routes, Route, Link, BrowserRouter } from 'react-router-dom';

function Header() {
    return (
      <header>
          <nav>
            <ul>
              <li><Link to="/main">Main</Link></li>
              <li><Link to="/favorites">Favorites</Link></li>
            </ul>
          </nav>
      </header>
    );
  }
  
  export default Header;
  