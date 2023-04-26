import React from 'react'
import { Link } from 'react-router-dom'

// let getTime = (word) => {
//     return new Date(word.updated).toLocaleDateString()
// }

// let getTitle = (word) => {
//     let title = word.body.split('\n')[0]
//     if (title.length > 45) {
//         return title.slice(0, 45)
//     }
//     return title
// }
//
// let getContent = (word) => {
//     let title = getTitle(word)
//     let content = word.body.replaceAll('\n', ' ')
//     content = content.replaceAll(title, '')
//
//     if (content.length > 45) {
//         return content.slice(0, 45) + '...'
//     }else{
//         return content
//     }
// }


const ListItem = ({ word }) => {
    return (
        <Link to={`/word/${word.id}`}>
            <div className="words-list-item">
                <h3>{word.english_writing}</h3>
                <p>{word.translation}</p>
            </div>
        </Link>
    )
}

export default ListItem
