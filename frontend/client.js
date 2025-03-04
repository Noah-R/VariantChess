import { createRoot } from "react-dom/client";
import React, { useState, useEffect } from "react";
import { io } from "socket.io-client";
import { Chessboard } from "react-chessboard";

const socket = io();

function App() {
	const [isConnected, setIsConnected] = useState(socket.connected);
	const [color, setColor] = useState("white");
	const [room, setRoom] = useState("");
	const [position, setPosition] = useState("start");
	const [status, setStatus] = useState("Not yet connected");

	useEffect(() => {
		function onConnect() {
			setIsConnected(true);
			console.log(`Connected with id: ${socket.id}`);
		}

		function onDisconnect() {
			setIsConnected(false);
			console.log(`Disconnected`);
		}

		function onPosition(data) {
			setPosition(data);
		}

		function onStatus(data) {
			setStatus(data);
		}

		function onMessage(data) {
			console.log("Received: " + data);
		}

		socket.on("connect", onConnect);
		socket.on("disconnect", onDisconnect);
		socket.on("position", onPosition);
		socket.on("status", onStatus);
		socket.on("message", onMessage);

		return () => {
			socket.off("connect", onConnect);
			socket.off("disconnect", onDisconnect);
			socket.off("position", onPosition);
			socket.off("message", onMessage);
		};
	}, []);

	function join(room, color){
		socket.emit("join", [room, color]);
		setColor(color);
	}

	const handleRoomChange = (event) => {
		setRoom(event.target.value);
	};

	
	function onDrop(sourceSquare, targetSquare, piece, promote = false) {
		let send = sourceSquare + targetSquare;
		if (promote) {
			send += piece;
		}
		socket.emit("move", send);
		return true;
	}

	function onPromote(piece, promoteFromSquare, promoteToSquare) {
		return onDrop(promoteFromSquare, promoteToSquare, piece, true);
	}

	return (
		<div>
			<input
				value={room}
				onChange={handleRoomChange}
				placeholder="Enter Room"
				maxlength="32"
			>
			</input>
			<button onClick={() => {join(room, "white")}}>White</button>
			<button onClick={() => {join(room, "black")}}>Black</button>
			<Chessboard
				id="Board"
				position={position}
				onPieceDrop={onDrop}
				onPromotionPieceSelect={onPromote}
				boardWidth={600}
				boardOrientation={color == "black" ? "black" : "white"}
			/>
			<h1>{status}</h1>
		</div>
	);
}

const domNode = document.getElementById("root");
const root = createRoot(domNode);
root.render(<App />);
