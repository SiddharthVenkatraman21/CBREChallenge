import logo from './logo.svg';
import './App.css';
import { createRoot } from 'react-dom/client';
import { Stage, Layer, Rect, Text, Circle, Line } from 'react-konva';
import ReactCSSTransitionGroup from 'react-transition-group'; 
import building from './building.png'

import Particles from "react-tsparticles";
import { Component } from 'react';
// import { Fade } from 'react-animation-components'



function Building(){
  return(
    <div className = "buildingClass">
      <img src={building} alt = "Building image" height = {500} width = {500}/>
    </div>
  );
}

function Rectangles(){
  return(
    <Stage width={window.innerWidth} height={window.innerHeight}>
      <Layer>
        
        <Rect
            x={50}
            y={25}
            width={200}
            height={100}
            // fill="red"
            stroke= "black"
            strokeWidth="5"
            // shadowBlur={10}
            border="black"
          />
          <Rect
            x={50}
            y={125}
            width={200}
            height={100}
            // fill="red"
            stroke= "black"
            strokeWidth="5"
            // shadowBlur={10}
            border="black"
          />
          <Rect
            x={50}
            y={225}
            width={200}
            height={100}
            // fill="red"
            stroke= "black"
            strokeWidth="5"
            // shadowBlur={10}
            border="black"
          />
          <Rect
            x={50}
            y={325}
            width={200}
            height={100}
            // fill="red"
            stroke= "black"
            strokeWidth="5"
            // shadowBlur={10}
            border="black"
          />
          <Rect
            x={50}
            y={425}
            width={200}
            height={100}
            // fill="red"
            stroke= "black"
            strokeWidth="5"
            // shadowBlur={10}
            border="black"
          />

          
          

          

        
      </Layer>
       
      </Stage>
  )
}

function Background() {
  return (
    <div className="App">
      <Particles
        options={{
          background: {
            color: "#181A18"
          },
          fpsLimit: 60,
          interactivity: {
            detectsOn: "canvas",
            events: {
              resize: true
            }
          },
          particles: {
            color: {
              value: "#ffffff"
            },
            number: {
              density: {
                enable: true,
                area: 1000
              },
              limit: 0,
              value: 300
            },
            opacity: {
              animation: {
                enable: true,
                minimumValue: 0.05,
                speed: 1,
                sync: false
              },
              random: {
                enable: true,
                minimumValue: 0.05
              },
              value: 1
            },
            shape: {
              type: "star"
            },
            size: {
              randmon: {
                enable: true,
                minimumValue: 0.5,
                value: 1
              }
            }
          }
        }}
      />
    </div>
  );
}

class Outline extends Component{
  state = {
    img: "./Outline.png"
  }
  render(){
    console.log(this.state.img)
  return(
    <div>
      <img src={this.state.img} alt = "outline image" height = {600} width = {600} className="outlineImage"
      onMouseEnter={() => {
        this.setState({
          img: "./outlineRed.png"
        })
      }}

      onMouseOut={() => {
        this.setState({
          img: "./Outline.png"
        })
      }}/>
      </div>
  );
  }

}



function App() {
  
    return (
      <div>
        <div className = "outlineDiv"> 
          <Outline/>
        </div>
        <div className ="Bottom">
          
        </div>
      </div>
      
    );
  

      

    

        


      
      

    
      

    
    
  
}

export default App;

