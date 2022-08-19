// отфильтруем книжки в зависимости от id автора методом useParams
import {useParams} from 'react-router-dom' // return object со всеми атрибутами

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
    var params = useParams()
    console.log(params.authorId) //  /authors/2 => 2
// отфильтруем по id
    var filteredBooks = books.filter((book) => book.authors.includes(parseInt(params.authorId))) // parseInt-преобразуем в str

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