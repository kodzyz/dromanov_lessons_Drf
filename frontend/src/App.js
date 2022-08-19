import React from 'react'
import AuthorList from './components/AuthorList.js'
import axios from 'axios'
import BookList from './components/BookList.js'

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

    render () {
        return (
            <div>
                 <AuthorList authors={this.state.authors} />
                 <BookList books={this.state.books} />
            </div>
        )
    }
}
export default App;