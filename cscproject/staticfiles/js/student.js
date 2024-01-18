import { onSidebarPopup } from './popup.js'
import { onImageUpload } from './image-upload.js'

if (document.getElementById('student-course-details')) {onSidebarPopup('#student-course-details')}

onImageUpload('[data-image="user"]', '#select-profile-image', 'input[type="submit"]')
