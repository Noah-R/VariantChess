import { useState } from "react";
import { Chessboard } from "react-chessboard";
import { PromotionPieceOption, Square } from "react-chessboard/dist/chessboard/types";

function App() {
	const [position, setPosition] = useState("start");

	function onDrop(
		sourceSquare: string | undefined,
		targetSquare: string | undefined,
		piece: string | undefined,
		promote: boolean = false
	) {
		const Http = new XMLHttpRequest();
		let url = "http://127.0.0.1:5000/" + sourceSquare + targetSquare;
		if (promote && piece) {
			url += piece.charAt(1);
		}
		Http.open("GET", url);
		Http.send();

		Http.onreadystatechange = (e) => {
			setPosition(Http.responseText);
			if(e){
				console.log(e);
			}
		};

		return true;
	}

	function onPromote(
		piece?: PromotionPieceOption | undefined,
		promoteFromSquare?: Square | undefined,
		promoteToSquare?: Square | undefined
	) {
		return onDrop(promoteFromSquare, promoteToSquare, piece, true);
	}

	return (
		<div>
			<Chessboard
				id="Board"
				position={position}
				onPieceDrop={onDrop}
				onPromotionPieceSelect={onPromote}
				boardWidth={600}
			/>
		</div>
	);
}

export default App;
