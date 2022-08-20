// разворачивание класса в лок переменную
import {useParams} from 'react-router-dom'

const BookItem = ({book}) => {
    return (
        <tr>
            <td>
                {book.title}
            </td>
            <td>
                {book.authors}
            </td>
        </tr>
    )
}

const AuthorBookList = ({books}) => {
    var {authorId} = useParams() // внутри объкта который вернул useParams берем поле authorId и присваиваем ее переменной authorId
    console.log(authorId)
    var filteredBooks = books.filter((book) => book.authors.includes(parseInt(authorId)))

    return (
        <table>
            <th>
                Title
            </th>
            <th>
                Authors
            </th>
            {filteredBooks.map((book) => <BookItem book={book} /> )}
        </table>
    )
}

export default AuthorBookList