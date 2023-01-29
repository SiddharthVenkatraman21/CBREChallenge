import logo from './logo.svg';
import './App.css';
import { createRoot } from 'react-dom/client';
import { Stage, Layer, Rect, Text, Circle, Line } from 'react-konva';
import ReactCSSTransitionGroup from 'react-transition-group'; 
import building from './building.png'
import Typewriter from 'typewriter-effect'
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

class floorStatsUpdate extends Component{
  state={
    floor: this.props.floorNum
  }
  render(){
    return(
      document.getElementById('floorStats').innerHTML = "testing"
    )
  }
}

class Outline extends Component{
  state = {
    img: this.props.image1
    
  }
  render(){
    console.log(this.state.img)
  return(
    
    <div className = "flexTest">
      
      <img src={this.state.img} alt = "outline image" height = {600} width = {600} className="outlineImage"
      onMouseEnter={() => {
        this.setState({
          img: this.props.image2
        })

        let floorval = "Floor: " + this.props.floor + 
        "<br>Team(s): " + this.props.teams + "<br>Population: " + this.props.Population + "<br>Floor Capacity: " + this.props.MaxCapacity
        document.getElementById('floorStats').innerHTML = floorval
       
      }
      }
      
      onMouseOut={() => {
        this.setState({
          img: this.props.image1
        })
      
        
        let genvar = "Teams Accomodated: 8/11 <br>Total Population: 336 <br>Total Capacity: 348 <br>Occupancy Level: 97%"
        document.getElementById('floorStats').innerHTML = genvar
        
      }}/>
      </div>
      
  );
  }

}



function App() {
  
    return (
      <div>

        


        <div className = "outlineDiv"> 
          <div className = "stack">
            <Outline image1="./build5.png" image2="./pic5new.png" floor="E" teams="6, 10" Population="93" MaxCapacity="97"/>
            <Outline image1="./build4.png" image2="./pic4new.png" floor="D" teams="4" Population="51" MaxCapacity="54"/>
            <Outline image1="./build3.png" image2="./pic1new.png" floor="C" teams="1, 11" Population="71" MaxCapacity="73"/>
            <Outline image1="./build2.png" image2="./pic2new.png" floor="B" teams="2, 3" Population="79" MaxCapacity="81"/>
            <Outline image1="./build1.png" image2="./pic3new.png" floor="A" teams="7" Population="43" MaxCapacity="45"/>
            </div>
        </div>
        


        <div className ="Bottom">
          <div className="typeWriterText">
            <Typewriter
              onInit={(typewriter) => {
                typewriter.typeString("CBRE Team Distribution").start()

              }}
              />
          </div>
          <div className="floorStats" id="floorStats">
          <Typewriter
              onInit={(typewriter) => {
                typewriter.typeString("Teams Accomodated: 8/11 <br></br>Total Population: 336 <br></br>Total Capacity: 348 <br></br>Occupancy Level: 97%").pauseFor(3000).start()
              }}
              />
            
          </div>
          
        </div>
      </div>
      
    );
  

      

    

        


      
      

    
      

    
    
  
}

export default App;

