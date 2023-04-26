import React, {useState, useEffect} from 'react'
import ListItem from "../components/ListItem.js";
import AddButton from "../components/AddButton.js";

const WordsListPage = () => {

    let [words, setWords] = useState([])

    useEffect(() => {
        getWords()
    }, [])

    let getWords = async () => {
        let response = await fetch('/api/words/')
        let data = await response.json()
        setWords(data)
    }

    return (
        <div className="words">
            <div className="words-header">
                <h2 className="words-title">&#9782; Words</h2>
                <p className="words-count">Number of all words: {words.length}</p>
            </div>
            <div className="words-list">
                {words.map((word, index) => (
                    <ListItem key={index} word={word} />
                ))}
            </div>
            <AddButton />
        </div>
    )
}

export default WordsListPage
