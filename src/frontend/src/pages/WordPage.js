import React, {useState, useEffect} from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { ReactComponent as ArrowLeft} from "../assets/chevron-left.svg";

const WordPage = () => {

    const { id } = useParams()
    const navigate = useNavigate();

    let [word, setWord] = useState(null);

    useEffect(() => {
        getWord()
    }, [id])

    let getWord = async () => {
        if (id === 'new') return
        let response = await fetch(`/api/words/${id}`)
        let data = await response.json()
        setWord(data)
    }

    let createWord = async () => {
        if (word.transcription === null) {
            word.transcription = ""
        }
        if (word.example === null) {
            word.example = ""
        }
        fetch(`/api/words/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(word)
        })
    }

    let updateWord = async () => {
        fetch(`/api/words/${id}/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(word)
        })
    }

    let deleteWord = async () => {
        fetch(`/api/words/${id}/`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            }
        })
        navigate(`/`);
    }

    let handleSubmit = () => {
        if (id !== 'new' && word.english_writing === "" && word.translation === "") {
            deleteWord()
        } else if (id !== 'new') {
            updateWord()
        } else if (id === 'new' && word.english_writing !== null && word.translation !== null) {
            createWord()
        }
        navigate(`/`);
    }

    return (
        <div className="word">
            <div className="word-header">
                <h3>
                    <ArrowLeft onClick={handleSubmit}/>
                </h3>
                {id !== 'new' ? (
                    <button onClick={deleteWord}>Delete</button>
                ): (
                    <button onClick={handleSubmit}>Done</button>
                )}
            </div>
            <div className="word-card-edit">
                <div className="word-card-english">
                    <textarea onChange={(e) => {setWord(word => ({ ...word, 'english_writing': e.target.value }))}} value={word?.english_writing}></textarea>
                </div>
                <div className="word-card-translation">
                    <textarea onChange={(e) => {setWord(word => ({ ...word, 'translation': e.target.value }))}} value={word?.translation}></textarea>
                </div>
            </div>
            <div className="word-additional-info">
                <div className="word-transcription">
                    <p> Transcription: </p>
                    <textarea onChange={(e) => {setWord(word => ({ ...word, 'transcription': e.target.value }))}} value={word?.transcription}></textarea>
                </div>
                <div className="word-example">
                    <p> Example:: </p>
                    <textarea onChange={(e) => {setWord(word => ({ ...word, 'example': e.target.value }))}} value={word?.example}></textarea>
                </div>
            </div>
        </div>
    )
}

export default WordPage
