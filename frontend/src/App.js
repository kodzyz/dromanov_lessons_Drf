import React from 'react'
import AuthorList from './components/AuthorList.js'
import axios from 'axios'
import BookList from './components/BookList.js'
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom'

class App extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            'authors': [],
            'books': []
        }
    }

    componentDidMount() {
        axios
        .get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                const authors = response.data
                    this.setState(  // меняем состояние компонента
                    {
                        'authors': authors
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/books/')
            .then(response => {
                const books = response.data
                this.setState(
                    {
                        'books': books
                    }
                )
            })
            .catch(error => console.log(error))
    }
//сделаем:
//a: при переходе по ссылке страница не перегружалась (single page application)
//b: меню навигации <nav> - генерим ссылки <Link to= на элементы Route <Route exact path=
//c: Link to= поддерживает как BrowserRouter так и HashRouter

    render () {
        return (
            <div>
                <BrowserRouter>
                     <nav>
                        <li> <Link to='/'>Authors</Link>< /li>
                        <li> <Link to='/books'> Books </Link> </li>
                     </nav>
                    <Routes>
                        <Route exact path='/' element={<AuthorList authors={this.state.authors} />} /> // exact- полное совпадение пути
                        <Route exact path='/books' element={<BookList books={this.state.books} />} />} /> //  BrowserRouter- http://localhost:3000/books
                    </Routes>
                 </BrowserRouter>
            </div>
        )
    }
}
export default App;