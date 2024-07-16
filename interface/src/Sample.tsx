import { useState } from "react";

interface Props {
	items: string[];
	heading: string;
	onSelectItem: (item: string) => void;
}

function Sample({ items, heading, onSelectItem }: Props) {
	const [selected, setSelected] = useState(-1);

	return (
		<>
			<h1>{heading}</h1>
			<ul className="list-group">
				{items.map((item, index) => (
					<li
						className={
							index === selected
								? "list-group-item active"
								: "list-group-item"
						}
						key={item}
						onClick={() => {
							setSelected(index);
							onSelectItem(item);
						}}
					>
						{item}
					</li>
				))}
			</ul>
		</>
	);
}

export default Sample;
