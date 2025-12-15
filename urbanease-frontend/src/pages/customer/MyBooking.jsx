import { useEffect, useState } from "react"
import axiosClient from "../../api/axiosClient"
import { useAuth } from "../../context/AuthContext"

export default function MyBookings() {
  const { user } = useAuth()
  const [bookings, setBookings] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    axiosClient
      .get("/bookings/")
      .then((res) => setBookings(res.data))
      .catch((err) => console.error(err))
      .finally(() => setLoading(false))
  }, [])
  console.log('bookings',bookings)
  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        Loading bookings...
      </div>
    )
  }

  if (bookings.length === 0) {
    return (
      <div className="min-h-screen flex items-center justify-center text-gray-500">
        No bookings found
      </div>
    )
  }

  return (
    <div className="container mx-auto px-4 py-8 max-w-5xl">
      <h1 className="text-2xl font-bold mb-6">
        My Bookings
      </h1>

      <div className="space-y-4">
        {bookings.map((booking) => (
          <div
            key={booking.id}
            className="bg-white shadow rounded-lg p-4 flex flex-col md:flex-row md:justify-between md:items-center"
          >
            {/* Left */}
            <div>
              <h3 className="font-semibold text-lg">
                {booking.service?.name || "Service"}
              </h3>
              <p className="text-sm text-gray-500">
                {new Date(booking.scheduled_at).toLocaleString()}
              </p>
              <p className="text-sm text-gray-500">
                {booking.address}
              </p>
            </div>

            {/* Right */}
            <div className="mt-3 md:mt-0">
              <span
                className={`px-3 py-1 rounded-full text-sm font-medium
                  ${
                    booking.status === "Completed"
                      ? "bg-green-100 text-green-700"
                      : booking.status === "Accepted"
                      ? "bg-blue-100 text-blue-700"
                      : "bg-yellow-100 text-yellow-700"
                  }
                `}
              >
                {booking.status}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
