import WordsListPage from "./WordsListPage.js";
import LessonListPage from "./LessonListPage";


function MainPage() {
    return (
        <div className="main-page">
            <WordsListPage />
            <LessonListPage />
        </div>
    );
}

export default MainPage
