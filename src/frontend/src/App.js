// import './App.css';
import Header from './components/Header.js';
import WordsListPage from "./pages/WordsListPage.js";
import {
  BrowserRouter as Router,
  Route,
  Routes
} from "react-router-dom";
import WordPage from "./pages/WordPage.js"

function App() {
  return (
      <Router>
        <div className="container dark">
          <div className="app">
            <Header />
            <Routes>
              <Route path="/" element={<WordsListPage />} />
              <Route path="/word/:id" element={<WordPage />} />
            </Routes>
          </div>
        </div>
      </Router>
  );
}

export default App;


