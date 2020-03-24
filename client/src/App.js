import React from 'react';
import './App.css';
import NavBar from './components/navbar.jsx'
import CourseList from './components/courses_list.jsx'
import CourseInfo from './components/course_info.jsx'
import styled from 'styled-components'

const FlexDiv = styled.div`
  display: flex;
  flex-direction: row;
`;

function App() {
  return (
    <div className="App">
      <NavBar>
          <FlexDiv>
            <CourseList/>
            <CourseInfo/>
            <div style={{width:'100%'}}></div>
            <div style={{width:'100%'}}></div>
            <div style={{width:'100%'}}></div>
          </FlexDiv>
      </NavBar>
    </div>
  );
}

export default App;
