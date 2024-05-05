// Get the canvas element.
const canvas = document.getElementById('pdf-canvas');

// Set the first page number to display
let pageNum = 1


// The PDF file URL. 
const pdfUrl = './sample.pdf';

//The URL is your main concern. Don;t touch anything below this line or you die
//******************************************************************************************************

const { pdfjsLib } = globalThis;

pdfjsLib.GlobalWorkerOptions.workerSrc = './pdf.worker.mjs';

function renderPage(pdfDoc, num) {
	pdfDoc
		.getPage(num)
		.then(function (page) {
			const viewport = page.getViewport({ scale: 1 });

			// Set the canvas dimensions to match the PDF page size.
			canvas.width = viewport.width;
			canvas.height = viewport.height;

			// Set the canvas rendering context.
			const ctx = canvas.getContext('2d');

			const renderContext = {
				canvasContext: ctx,
				viewport: viewport,
			};

			// Render the PDF page to the canvas.
			page.render(renderContext);
		})
		.then(function () {
			console.log('Rendering complete');
		});
}

// Load the PDF file using PDF.js.
pdfjsLib.getDocument(pdfUrl).promise.then(function (pdfDoc) {
	// Get the first page of the PDF file.
	renderPage(pdfDoc, pageNum)
}).catch(function (error) {
	alert('Error opening PDF file')
	console.log('Error loading PDF file:', error);
});

// Event listeners for navigation controls
document.getElementById('prev-page').addEventListener('click', function() {

    pdfjsLib.getDocument(pdfUrl).promise.then(function (pdfDoc) {
		if (pageNum <= 1) {
			return;
		}
		pageNum--;
		renderPage(pdfDoc, pageNum)
	}).catch(function (error) {
		alert('Error opening PDF file')
		console.log('Error loading PDF file:', error);
	});
});

document.getElementById('next-page').addEventListener('click', function() {

    pdfjsLib.getDocument(pdfUrl).promise.then(function (pdfDoc) {

		if (pageNum >= pdfDoc.numPages) {
			return;
		}
		pageNum++;
		renderPage(pdfDoc, pageNum)
	}).catch(function (error) {
		alert('Error opening PDF file')
		console.log('Error loading PDF file:', error);
	});
});