import './App.css';
import Header from './components/Header.js';
import {
  BrowserRouter as Router,
  Route,
  Routes
} from "react-router-dom";
import WordPage from "./pages/WordPage.js"
import MainPage from "./pages/MainPage";
// import LessonPage from "./pages/LessonPage";
import WordsListPage from "./pages/WordsListPage";

function App() {
  return (
      <Router>
        <div className="container light">
          <div className="app">
            <Header />
            <Routes>
              <Route path="/" element={<WordsListPage />} />
              <Route path="/word/:id" element={<WordPage />} />
              {/*<Route path="/lesson/:id" element={<LessonPage />}/>*/}
            </Routes>
          </div>
        </div>
      </Router>
  );
}

export default App;


