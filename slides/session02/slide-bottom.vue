<template>
  <footer style="font-size: 8pt">
    <div class="absolute bottom-0 left-0 p-2">Session 02 &bull; Alok Menghrajani</div>
    <div v-if="$nav.currentPage !== 1" class="absolute bottom-0 left-0 right-0 p-2" style="text-align: center"><SlideCurrentNo /> / <SlidesTotal /></div>
    <div v-if="$nav.currentPage !== 1" class="absolute bottom-0 right-0 p-2">EPFL &bull; CIVIL-127 &bull; 2025</div>
  </footer>
</template>
