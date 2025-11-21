const CACHE_NAME = 'airaware-cache-v1';
const urlsToCache = [
    '/',
    '/manifest.json',
    // We cache the sample AQI data for the initial offline load
    '/api/aqi?city=delhi', 
    '/api/cities'
];

self.addEventListener('install', (event) => {
    // Perform install steps
    event.waitUntil(
        caches.open(CACHE_NAME)
        .then((cache) => {
            console.log('Opened cache');
            return cache.addAll(urlsToCache).catch(error => {
                console.error('Failed to cache resources:', error);
            });
        })
    );
    self.skipWaiting();
});

self.addEventListener('fetch', (event) => {
    // Strategy: Cache-first for shell, Network-first for API
    const url = new URL(event.request.url);

    // Cache-first strategy for the main file
    if (url.pathname === '/') {
        event.respondWith(
            caches.match(event.request)
            .then(response => response || fetch(event.request))
        );
        return;
    }

    // Network-first strategy for APIs (to get freshest data, falling back to cache)
    if (url.pathname.startsWith('/api/')) {
        event.respondWith(
            fetch(event.request).catch(() => {
                // Fallback to cache on network failure
                return caches.match(event.request);
            })
        );
        return;
    }

    // Default: Cache-first for other static assets
    event.respondWith(
        caches.match(event.request)
        .then(response => response || fetch(event.request))
    );
});

self.addEventListener('activate', (event) => {
    // Delete old caches
    const cacheWhitelist = [CACHE_NAME];
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheWhitelist.indexOf(cacheName) === -1) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
    return self.clients.claim();
});
