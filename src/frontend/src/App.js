import './App.css';
import Header from './components/Header.js';
import {
  BrowserRouter as Router,
  Route,
  Routes
} from "react-router-dom";
import WordPage from "./pages/WordPage.js"
import MainPage from "./pages/MainPage";

function App() {
  return (
      <Router>
        <div className="container light">
          <div className="app">
            <Header />
            <Routes>
              <Route path="/" element={<MainPage />} />
              <Route path="/word/:id" element={<WordPage />} />
            </Routes>
          </div>
        </div>
      </Router>
  );
}

export default App;


