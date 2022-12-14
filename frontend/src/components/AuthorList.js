import {Link} from 'react-router-dom'
//сделаем:
//1. кликая на автора из списка попадаем на список его книжек
//Link to={`/authors/${author.id}`} : обратные кавычки - аналог f-строки python

const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>
                {author.first_name}
            </td>
            <td>
                <Link to={`/authors/${author.id}`}>{author.last_name}</Link>
            </td>
            <td>
                {author.birthday_year}
            </td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                Birthday year
            </th>
            {authors.map((author) => <AuthorItem author={author} /> )}
        </table>
    )
}

export default AuthorList