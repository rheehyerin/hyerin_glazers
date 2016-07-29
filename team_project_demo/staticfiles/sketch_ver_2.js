var song, rms;

var numOfInnerCircles;
var numOfOuterCircels;
var scale;
var sum;
var smoothFactor;
var x=[];
var y=[];
var outCirclesR=[];
var speed=[];
var circleColor=[];
var level;
var radius;
var angle;
var r;
var outerCircleSmooth;

function preload(){
    song = loadSound("static/assets/lifeincolor.mp3");
}

function setup(){
    createCanvas(900, 900);

    sum=0;
    radius=5;
    scale=3;
    smoothFactor=0.157;
    numOfInnerCircles=5;
    numOfOuterCircels=7;
    outerCircleSmooth=0.05;
    anlge=0;
    r=0;
    outerCircleSmooth=0.05;

    song.play();
    rms = new p5.Amplitude();
    rms.setInput(song);

    for(var i=0; i<numOfInnerCircles; i++){
        x[i]=0;
        y[i]=0;
    }

    for(var i=0; i<numOfOuterCircels; i++){
        outCirclesR[i]=0;
    }

    for(var i=0; i<numOfOuterCircels; i++){
        speed[i] =random(1, 5);
    }
}

function draw(){
    background(0);
    sum += (rms.getLevel()-sum)*smoothFactor;
    radius = sum*150*scale;


    for(var i=0; i<numOfInnerCircles; i++){
        x[i] = radius*cos(TWO_PI/numOfInnerCircles*i)*1.5;
        y[i] = radius*sin(TWO_PI/numOfInnerCircles*i)*1.5;
        strokeWeight(9);
        stroke(255, 90);
        applyMatrix();
        translate(width/2, height/2);
        point(x[i], y[i]);
        resetMatrix();
    }
    /*
    applyMatrix();
    translate(width/2, height/2);
    stroke(255, 50);

    rotateX(radians(angle*2));
    retateY(radians(angle*2));
    r = 1/sum;
    if (parseInt(r) < 15){
        r = (1/r)*300;
        sphere(r, parseInt(sum*20));
    }else{
        sphere(r*5, parseInt(sum*20));
    }
    angle++;
    resetMatrix();
    */

    if(sum>outerCircleSmooth){
        for(var i=0; i<numOfOuterCircels; i++){
            outCirclesR[i] += speed[i];
            if(outCirclesR[i]>(width*1.5)){
                outCirclesR[i]=0;
            }

            stroke(parseInt(random(1, 255)), parseInt(random(1, 255)), parseInt(random(1, 255)));
            strokeWeight(1);
            noFill();
            ellipse(width/2, height/2, outCirclesR[i], outCirclesR[i]);
        }

    }

}



