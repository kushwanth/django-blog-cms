import  React, { Component } from  'react';
import { BrowserRouter } from 'react-router-dom'
import { Route } from 'react-router-dom'

import postsdetail from './postdetail'
import postslist from './postlist'

const BaseLayout = () => (
    <div className="content">
      <Route path="/" exact component={postslist} />
      <Route path="/:slug"  component={postsdetail} />
    </div>
)

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <BaseLayout/>
      </BrowserRouter>
    );
  }
}

export default App;
