// 0:49 обработчик получения token
import React from 'react'
import AuthorList from './components/AuthorList.js'
import axios from 'axios'
import BookList from './components/BookList.js'
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom'
import AuthorBookList from './components/AuthorBookList.js'
import LoginForm from './components/LoginForm.js'


const NotFound = () => {
    var {pathname} = useLocation() // инфо о странице

    return (
        <div>
            Page "{pathname}" not found
        </div>
    )
}

class App extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            'authors': [],
            'books': []
        }
    }

    obtainAuthToken(login, password) {
        console.log('obtainAuthToken:', login, password)
    }

    componentDidMount() {
        axios
        .get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                const authors = response.data
                    this.setState(
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


    render () {
        return (
            <div>
                <BrowserRouter>
                     <nav>
                        <li> <Link to='/'>Authors</Link>< /li>
                        <li> <Link to='/books'> Books </Link> </li>
                        <li> <Link to='/login'> login </Link> </li>
                     </nav>
                    <Routes>
                    <Route exact path='/' element={<Navigate to='/authors' />} />
                        <Route exact path='/books' element={<BookList books={this.state.books} authors={this.state.authors} />} />
                        <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)} />} />

                        <Route path='/authors'>
                            <Route index element={<AuthorList authors={this.state.authors} />} />
                            <Route path=':authorId' element={<AuthorBookList books={this.state.books} />} />
                        </Route>
                            <Route path='*' element={<NotFound />} />
                    </Routes>
                 </BrowserRouter>
            </div>
        )
    }
}
export default App;