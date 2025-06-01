import React, {useState, useEffect} from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { ReactComponent as ArrowLeft} from "../assets/chevron-left.svg";
import { ReactComponent as TranslationButton} from "../assets/translation-arrow.svg";

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
        if (word.transcription === undefined) {
            word.transcription = ""
        }
        if (word.example === undefined) {
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

    let isFormValid = () => {
        return word && 
               word.english_writing && 
               word.english_writing.trim() !== "" && 
               word.translation && 
               word.translation.trim() !== "";
    }

    let handleSubmit = () => {
        if (id !== 'new' && word.english_writing === "" && word.translation === "") {
            deleteWord()
        } else if (id !== 'new') {
            if (isFormValid()) {
                updateWord()
                navigate(`/`);
            } else {
                alert("Please fill in both English word and translation fields");
                return;
            }
        } else if (id === 'new' && word !== null) {
            if (isFormValid()) {
                createWord()
                navigate(`/`);
            } else {
                alert("Please fill in both English word and translation fields");
                return;
            }
        } else {
            navigate(`/`);
        }
    }

    let showTranslation = () => {
        let EnglishWord = document.querySelector('.word-card-english');
        let EnglishWordCard = document.querySelector('.word-card-english > textarea');
        let TranslationWord = document.querySelector('.word-card-translation');
        let TranslationWordCard = document.querySelector('.word-card-translation > textarea');
        if (EnglishWord.classList.contains('word-card-cover')) {
            EnglishWord.classList.remove('word-card-cover');
            EnglishWordCard.style.display = 'inline-block';
            TranslationWord.classList.add('word-card-cover');
            TranslationWordCard.style.display = 'none';
        } else {
            TranslationWord.classList.remove('word-card-cover');
            TranslationWordCard.style.display = 'inline-block';
            EnglishWord.classList.add('word-card-cover');
            EnglishWordCard.style.display = 'none';
        }
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
                    <textarea 
                        placeholder="Введите слово на английском" 
                        required 
                        onChange={(e) => {setWord(word => ({ ...word, 'english_writing': e.target.value }))}} 
                        value={word?.english_writing || ''}
                    ></textarea>
                </div>
                <TranslationButton onClick={showTranslation} />
                <div className="word-card-translation word-card-cover">
                    <textarea 
                        placeholder="Введите перевод слова" 
                        required 
                        style={{display: 'none'}} 
                        onChange={(e) => {setWord(word => ({ ...word, 'translation': e.target.value }))}} 
                        value={word?.translation || ''}
                    ></textarea>
                </div>
            </div>
            <div className="word-additional-info">
                <div className="word-transcription">
                    <p> Transcription: </p>
                    <textarea 
                        placeholder="Введите транскрипцию слова (при наличии)" 
                        onChange={(e) => {setWord(word => ({ ...word, 'transcription': e.target.value }))}} 
                        value={word?.transcription || ''}
                    ></textarea>
                </div>
                <div className="word-example">
                    <p> Example: </p>
                    <textarea 
                        placeholder="Введите пример с использованием слова (при наличии)" 
                        onChange={(e) => {setWord(word => ({ ...word, 'example': e.target.value }))}} 
                        value={word?.example || ''}
                    ></textarea>
                </div>
            </div>
        </div>
    )
}

export default WordPage