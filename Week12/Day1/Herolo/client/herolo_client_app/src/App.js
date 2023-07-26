import './App.css';
import Header from './components/Header';
import { Routes, Route, Link } from "react-router-dom";
import Main from './components/Main';
import Favorites from './components/Favorites';

function App() {
  return (
    <div>
      <Header />
      <Routes>
        <Route path="/main" element={<Main />} />
        <Route path="/favorites" element={<Favorites />} />
      </Routes>
    </div>
  );
}

export default App;
