methods {
	eventsMap(uint16) returns (address, uint64, uint16) envfree;
}

function getRemainingTickets(uint16 eventIndex) returns uint16 {
    address owner; uint64 ticketPrice; uint16 ticketsRemaining;
    owner, ticketPrice, ticketsRemaining = eventsMap(eventIndex);
    return ticketsRemaining;
}

function getOwner(uint16 eventIndex) returns address {
    address owner; uint64 ticketPrice; uint16 ticketsRemaining;
    owner, ticketPrice, ticketsRemaining = eventsMap(eventIndex);
    return owner;
}

function getTicketPrice(uint16 eventIndex) returns uint64 {
    address owner; uint64 ticketPrice; uint16 ticketsRemaining;
    owner, ticketPrice, ticketsRemaining = eventsMap(eventIndex);
    return ticketPrice;
}

rule monotonicityOfNumberOfEvents(method f) {
	env e; calldataarg args;

	uint16 numberOfEventsBefore = numEvents(e);

	f(e, args);
	
	uint16 numberOfEventsAfter = numEvents(e);
	assert numberOfEventsAfter >= numberOfEventsBefore, "number of events decreased";
}

rule ownerImmutability(method f, uint16 eventId) {
	env e; calldataarg args;

	address ownerBefore = getOwner(eventId);

	f(e, args);
	
	address ownerAfter = getOwner(eventId);
	assert ownerAfter == ownerBefore, "owner changed";
}

rule monotonicityOfRemainingTickets(method f, uint16 eventId) {
	env e; calldataarg args;

	uint16 remainingTicketsBefore = getRemainingTickets(eventId);
	uint16 numberOfEvents = numEvents(e);
	require numberOfEvents >= eventId;

	f(e, args);
	
	uint16 remainingTicketsAfter = getRemainingTickets(eventId);
	assert remainingTicketsAfter <= remainingTicketsBefore, "number of remaining tickets increased";
}

rule ticketPriceCantBeManipulated(method f, uint16 eventId) {
		env e; calldataarg args;

		uint64 ticketPriceBefore = getTicketPrice(eventId);
		
		f(e, args);

		uint64 ticketPriceAfter = getTicketPrice(eventId);
		assert ticketPriceAfter == ticketPriceBefore, "ticket price changed";
}