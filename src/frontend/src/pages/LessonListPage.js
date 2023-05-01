import React, {useState, useEffect} from 'react'
import ListItem from "../components/ListItem.js";
import AddButton from "../components/AddButton.js";

const LessonListPage = () => {

    let [lessons, setLessons] = useState([])

    useEffect(() => {
        getLessons()
    }, [])

    let getLessons = async () => {
        let response = await fetch('/api/lessons/')
        let data = await response.json()
        setLessons(data)
    }

    return (
        <div className="words">
            <div className="words-header">
                <h2 className="words-title">&#9782; Lessons</h2>
                <p className="words-count">Number of lessons: {lessons.length}</p>
            </div>
            <div className="words-list">
                {lessons.map((lesson, index) => (
                    <ListItem key={index} word={lesson} />
                ))}
            </div>
            <AddButton link={"/lesson/new"}/>
        </div>
    )
}

export default LessonListPage
